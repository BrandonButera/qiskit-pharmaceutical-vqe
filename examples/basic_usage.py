"""
Basic usage example for qiskit-pharmaceutical-vqe.

This example demonstrates how to use the pharma_vqe package to:
1. Initialize a molecular simulator
2. Run VQE optimization
3. Calculate molecular properties
"""

from pharma_vqe import VQEAlgorithm, MolecularSimulator
from pharma_vqe.molecular_simulator import MoleculeType
import numpy as np


def main() -> None:
    """Run basic example of VQE for pharmaceutical applications."""

    print("=" * 70)
    print("Quantum VQE for Pharmaceutical Drug Discovery")
    print("=" * 70)

    # Step 1: Initialize molecular simulator
    print("\n[Step 1] Initializing Molecular Simulator...")
    simulator = MolecularSimulator(molecule_type=MoleculeType.H2)
    print(f"Molecule: H2")
    print(f"Simulator initialized successfully!")

    # Step 2: Get circuit information
    print("\n[Step 2] Getting VQE Circuit Information...")
    num_qubits = simulator.get_vqe_circuit_qubits()
    print(f"Number of qubits required: {num_qubits}")

    # Step 3: Initialize VQE algorithm
    print("\n[Step 3] Initializing VQE Algorithm...")
    vqe = VQEAlgorithm(num_qubits=num_qubits, num_layers=1)
    print(f"VQE algorithm initialized with {num_qubits} qubits and 1 layer")

    # Step 4: Prepare initial parameters
    print("\n[Step 4] Preparing Initial Parameters...")
    initial_params = simulator.prepare_quantum_circuit_params()
    print(f"Initial rotation angles shape: {initial_params.shape}")
    print(f"Initial parameters: {initial_params[:3]}...")  # Show first 3

    # Step 5: Run optimization
    print("\n[Step 5] Running VQE Optimization...")
    print("Note: This is a demonstration. Real optimization may take longer.")
    optimized_params, min_energy = vqe.optimize(initial_params)
    print(f"Optimization complete!")
    print(f"Minimum energy found: {min_energy:.6f} Hartree")

    # Step 6: Validate results
    print("\n[Step 6] Validating Results...")
    is_valid = simulator.validate_vqe_result(min_energy)
    status = "✓ Valid" if is_valid else "✗ Invalid"
    print(f"Result validation: {status}")

    # Step 7: Calculate properties
    print("\n[Step 7] Calculating Molecular Properties...")
    properties = simulator.calculate_properties_from_energy(min_energy)
    print(f"Ground State Energy: {properties['ground_state_energy']:.6f} Hartree")
    print(f"Energy Error: {properties['energy_error']:.6f} Hartree")
    print(f"Binding Affinity: {properties['binding_affinity']:.2f} kcal/mol")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Molecule: H2")
    print(f"VQE Ground State Energy: {min_energy:.6f} Hartree")
    print(f"Convergence Status: {'Converged' if is_valid else 'Not Converged'}")
    print("=" * 70)


if __name__ == "__main__":
    main()
  
