"""
Molecular Simulation Utilities for Pharmaceutical Applications

This module provides utilities for preparing molecular systems, calculating
molecular properties, and interfacing with quantum simulators for drug discovery.
"""

from typing import Dict, List, Tuple, Optional
import numpy as np
from dataclasses import dataclass
from enum import Enum


class MoleculeType(Enum):
      """Enumeration of supported molecule types."""
      H2 = "hydrogen_molecule"
      H2O = "water_molecule"
      NH3 = "ammonia"
      CH4 = "methane"
      CUSTOM = "custom"


@dataclass
class MolecularProperties:
    """Data class for storing molecular properties."""
    name: str
    molecular_weight: float
    ground_state_energy: float  # in Hartree
    num_electrons: int
    num_orbitals: int
    bond_length: float  # in Angstroms
    binding_affinity: Optional[float] = None  # in kcal/mol


class MolecularSimulator:
    """
    Quantum molecular simulator for pharmaceutical drug discovery.

    This class manages molecular systems and interfaces with VQE algorithms
    to compute molecular properties including ground state energies, binding
    affinities, and molecular interactions.
    """

    # Predefined molecular properties
    MOLECULES: Dict[MoleculeType, MolecularProperties] = {
        MoleculeType.H2: MolecularProperties(
            name="Hydrogen Molecule",
            molecular_weight=2.016,
            ground_state_energy=-1.17,  # Hartree
            num_electrons=2,
            num_orbitals=2,
            bond_length=0.74  # Angstroms
        ),
        MoleculeType.H2O: MolecularProperties(
            name="Water Molecule",
            molecular_weight=18.015,
            ground_state_energy=-76.4,  # Hartree (approximate)
            num_electrons=10,
            num_orbitals=7,
            bond_length=0.96  # O-H bond length
        ),
        MoleculeType.NH3: MolecularProperties(
            name="Ammonia",
            molecular_weight=17.031,
            ground_state_energy=-56.5,  # Hartree (approximate)
            num_electrons=10,
            num_orbitals=7,
            bond_length=1.01  # N-H bond length
        ),
        MoleculeType.CH4: MolecularProperties(
            name="Methane",
            molecular_weight=16.043,
            ground_state_energy=-40.2,  # Hartree (approximate)
            num_electrons=10,
            num_orbitals=9,
            bond_length=1.09  # C-H bond length
        ),
    }

    def __init__(self, molecule_type: MoleculeType = MoleculeType.H2):
        """
        Initialize molecular simulator.

        Args:
            molecule_type: Type of molecule to simulate
        """
        self.molecule_type = molecule_type
        self.properties = self.MOLECULES.get(
            molecule_type,
            MolecularProperties(
                name="Unknown",
                molecular_weight=0.0,
                ground_state_energy=0.0,
                num_electrons=0,
                num_orbitals=0,
                bond_length=0.0
            )
        )
        self.computed_properties: Dict[str, float] = {}

    def get_hamiltonian_coefficients(self) -> Tuple[float, float]:
        """
        Get Hamiltonian coefficients for VQE circuit.

        For H2 molecule VQE:
            - Diagonal terms (qubit 0 and 1): 0.2 + 0.2 = 0.4
            - Off-diagonal (entangling) term: -0.2

        Returns:
            Tuple of (diagonal_coeff, off_diagonal_coeff)
        """
        if self.molecule_type == MoleculeType.H2:
            return 0.2, -0.2
        else:
            # Generic coefficients for other molecules
            return 0.1, -0.1

    def prepare_quantum_circuit_params(self) -> np.ndarray:
        """
        Prepare initial parameters for quantum circuit.

        Returns:
            Array of initial rotation angles
        """
        num_qubits = self.properties.num_electrons
        return np.random.uniform(0, 2*np.pi, num_qubits)

    def calculate_binding_affinity(self, vqe_energy: float) -> float:
        """
        Calculate binding affinity from VQE ground state energy.

        Binding affinity is estimated as the energy difference relative
        to reference state, converted to kcal/mol.

        Hartree to kcal/mol conversion: 1 Hartree ≈ 627.51 kcal/mol

        Args:
            vqe_energy: Ground state energy from VQE in Hartree

        Returns:
            Binding affinity in kcal/mol
        """
        HARTREE_TO_KCAL_MOL = 627.51

        # Reference energy (classical DFT result)
        reference_energy = self.properties.ground_state_energy

        # Energy difference
        delta_e = vqe_energy - reference_energy

        # Convert to kcal/mol
        affinity = delta_e * HARTREE_TO_KCAL_MOL

        return affinity

    def validate_vqe_result(self, vqe_energy: float) -> bool:
        """
        Validate VQE result against expected ground state energy.

        For H2: Expected ground state energy = -1.17 Hartree
            - Results validated against classical method (DFT)
            - No guarantee of efficiency/binding (exploratory tool)

        Args:
            vqe_energy: Ground state energy from VQE

        Returns:
            True if result is reasonable, False otherwise
        """
        expected = self.properties.ground_state_energy
        tolerance = 0.1  # ±0.1 Hartree tolerance

        difference = abs(vqe_energy - expected)
        is_valid = difference < tolerance

        # Store result
        self.computed_properties["vqe_energy"] = vqe_energy
        self.computed_properties["energy_error"] = difference
        self.computed_properties["is_valid"] = is_valid

        return is_valid

    def get_molecular_info(self) -> str:
        """
        Get formatted molecular information.

        Returns:
            Formatted string with molecule properties
        """
        return f"""
Molecular System: {self.properties.name}
- Molecular Weight: {self.properties.molecular_weight} g/mol
- Ground State Energy: {self.properties.ground_state_energy} Hartree
- Number of Electrons: {self.properties.num_electrons}
- Number of Quantum Orbitals: {self.properties.num_orbitals}
- Bond Length: {self.properties.bond_length} Å
"""

    def get_vqe_circuit_qubits(self) -> int:
        """
        Get number of qubits needed for VQE circuit.

        Returns:
            Number of qubits required
        """
        # For most small molecules, use electron count as qubits
        return self.properties.num_electrons

    def estimate_convergence_iterations(self) -> int:
        """
        Estimate number of iterations needed for VQE convergence.

        Based on molecular complexity and circuit depth.

        Returns:
            Estimated iterations for convergence
        """
        # Simple heuristic: 100-200 iterations per electron
        num_electrons = self.properties.num_electrons
        return 100 + (50 * num_electrons)

    def calculate_properties_from_energy(self, vqe_energy: float) -> Dict[str, float]:
        """
        Calculate derived molecular properties from VQE energy.

        Args:
            vqe_energy: Ground state energy from VQE in Hartree

        Returns:
            Dictionary of calculated properties
        """
        properties = {
            "ground_state_energy": vqe_energy,
            "binding_affinity": self.calculate_binding_affinity(vqe_energy),
            "energy_error": abs(vqe_energy - self.properties.ground_state_energy),
        }

        self.computed_properties.update(properties)
        return properties
