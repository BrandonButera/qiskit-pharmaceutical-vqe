"""
Unit tests for Molecular Simulator module.

Tests the MolecularSimulator implementation for pharmaceutical applications.
"""

import pytest
import numpy as np
from pharma_vqe.molecular_simulator import (
    MolecularSimulator,
    MoleculeType,
    MolecularProperties
)


class TestMolecularSimulator:
    """Test cases for MolecularSimulator class."""

    @pytest.fixture
    def h2_simulator(self) -> MolecularSimulator:
        """Create a MolecularSimulator instance for H2."""
        return MolecularSimulator(molecule_type=MoleculeType.H2)

    @pytest.fixture
    def h2o_simulator(self) -> MolecularSimulator:
        """Create a MolecularSimulator instance for H2O."""
        return MolecularSimulator(molecule_type=MoleculeType.H2O)

    def test_initialization_h2(self, h2_simulator: MolecularSimulator) -> None:
        """Test MolecularSimulator initialization for H2."""
        assert h2_simulator is not None
        assert h2_simulator.molecule_type == MoleculeType.H2
        assert h2_simulator.properties.name == "Hydrogen Molecule"
        assert h2_simulator.properties.num_electrons == 2
        assert h2_simulator.properties.ground_state_energy == -1.17

    def test_initialization_h2o(self, h2o_simulator: MolecularSimulator) -> None:
        """Test MolecularSimulator initialization for H2O."""
        assert h2o_simulator is not None
        assert h2o_simulator.molecule_type == MoleculeType.H2O
        assert h2o_simulator.properties.name == "Water Molecule"
        assert h2o_simulator.properties.num_electrons == 10

    def test_get_molecular_info(self, h2_simulator: MolecularSimulator) -> None:
        """Test getting molecular information."""
        info = h2_simulator.get_molecular_info()
        assert "Hydrogen Molecule" in info
        assert "2.016" in info
        assert "-1.17" in info
        assert "2" in info  # num_electrons
        assert "0.74" in info  # bond_length

    def test_get_vqe_circuit_qubits(self, h2_simulator: MolecularSimulator) -> None:
        """Test getting number of qubits required."""
        num_qubits = h2_simulator.get_vqe_circuit_qubits()
        assert num_qubits == 2  # H2 has 2 electrons

    def test_prepare_quantum_circuit_params(self, h2_simulator: MolecularSimulator) -> None:
        """Test preparation of quantum circuit parameters."""
        params = h2_simulator.prepare_quantum_circuit_params()
        assert isinstance(params, np.ndarray)
        assert params.shape == (2,)  # 2 electrons -> 2 parameters
        assert all(0 <= p <= 2*np.pi for p in params)

    def test_get_hamiltonian_coefficients_h2(self, h2_simulator: MolecularSimulator) -> None:
        """Test getting Hamiltonian coefficients for H2."""
        diagonal, off_diagonal = h2_simulator.get_hamiltonian_coefficients()
        assert diagonal == 0.2
        assert off_diagonal == -0.2

    def test_get_hamiltonian_coefficients_other(self, h2o_simulator: MolecularSimulator) -> None:
        """Test getting Hamiltonian coefficients for non-H2 molecules."""
        diagonal, off_diagonal = h2o_simulator.get_hamiltonian_coefficients()
        assert diagonal == 0.1
        assert off_diagonal == -0.1

    def test_calculate_binding_affinity(self, h2_simulator: MolecularSimulator) -> None:
        """Test binding affinity calculation."""
        vqe_energy = -1.15  # Close to ground state
        affinity = h2_simulator.calculate_binding_affinity(vqe_energy)

        # Energy difference: -1.15 - (-1.17) = 0.02 Hartree
        # In kcal/mol: 0.02 * 627.51 ≈ 12.55
        assert isinstance(affinity, float)
        assert abs(affinity - 12.55) < 1.0  # Allow some tolerance

    def test_validate_vqe_result_valid(self, h2_simulator: MolecularSimulator) -> None:
        """Test validation of a valid VQE result."""
        vqe_energy = -1.15  # Within 0.1 Hartree tolerance
        is_valid = h2_simulator.validate_vqe_result(vqe_energy)
        assert is_valid is True
        assert "vqe_energy" in h2_simulator.computed_properties
        assert h2_simulator.computed_properties["is_valid"] is True

    def test_validate_vqe_result_invalid(self, h2_simulator: MolecularSimulator) -> None:
        """Test validation of an invalid VQE result."""
        vqe_energy = -0.5  # Far from expected -1.17
        is_valid = h2_simulator.validate_vqe_result(vqe_energy)
        assert is_valid is False
        assert h2_simulator.computed_properties["is_valid"] is False

    def test_estimate_convergence_iterations(self, h2_simulator: MolecularSimulator) -> None:
        """Test estimation of convergence iterations."""
        iterations = h2_simulator.estimate_convergence_iterations()
        # For H2: 100 + (50 * 2) = 200
        assert iterations == 200

    def test_calculate_properties_from_energy(self, h2_simulator: MolecularSimulator) -> None:
        """Test calculation of properties from VQE energy."""
        vqe_energy = -1.15
        properties = h2_simulator.calculate_properties_from_energy(vqe_energy)

        assert "ground_state_energy" in properties
        assert "binding_affinity" in properties
        assert "energy_error" in properties

        assert properties["ground_state_energy"] == vqe_energy
        assert abs(properties["energy_error"] - 0.02) < 0.001

    @pytest.mark.parametrize("molecule_type,expected_electrons", [
        (MoleculeType.H2, 2),
        (MoleculeType.H2O, 10),
        (MoleculeType.NH3, 10),
        (MoleculeType.CH4, 10),
    ])
    def test_various_molecules(self, molecule_type: MoleculeType, expected_electrons: int) -> None:
        """Test MolecularSimulator with various molecule types."""
        simulator = MolecularSimulator(molecule_type=molecule_type)
        assert simulator.properties.num_electrons == expected_electrons
        assert simulator.get_vqe_circuit_qubits() == expected_electrons

    def test_molecular_properties_dataclass(self) -> None:
        """Test MolecularProperties dataclass."""
        props = MolecularProperties(
            name="Test Molecule",
            molecular_weight=10.0,
            ground_state_energy=-5.0,
            num_electrons=4,
            num_orbitals=3,
            bond_length=1.0,
            binding_affinity=10.0
        )
        assert props.name == "Test Molecule"
        assert props.molecular_weight == 10.0
        assert props.binding_affinity == 10.0

    def test_unknown_molecule_type(self) -> None:
        """Test handling of unknown molecule type."""
        # This should use the default unknown molecule
        simulator = MolecularSimulator(molecule_type=MoleculeType.CUSTOM)
        assert simulator.properties.name == "Unknown"
        assert simulator.properties.num_electrons == 0
