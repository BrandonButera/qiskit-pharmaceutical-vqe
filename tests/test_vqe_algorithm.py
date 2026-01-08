"""
Unit tests for VQE Algorithm module.

Tests the Variational Quantum Eigensolver implementation
for pharmaceutical applications.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock, patch
from pharma_vqe.vqe_algorithm import VQEAlgorithm


class TestVQEAlgorithm:
      """Test cases for VQEAlgorithm class."""

    @pytest.fixture
    def vqe_instance(self) -> VQEAlgorithm:
              """Create a VQEAlgorithm instance for testing."""
              return VQEAlgorithm(num_qubits=2, num_layers=1)

    def test_initialization(self, vqe_instance: VQEAlgorithm) -> None:
              """Test VQEAlgorithm initialization."""
              assert vqe_instance is not None
              assert vqe_instance.num_qubits == 2
              assert vqe_instance.num_layers == 1

    def test_optimize_with_mock_data(self, vqe_instance: VQEAlgorithm) -> None:
              """Test VQE optimization with mock data."""
              initial_params = np.array([0.1, 0.2])

        with patch.object(vqe_instance, 'optimize', return_value=(np.array([0.15, 0.25]), -1.5)):
                      optimized_params, min_energy = vqe_instance.optimize(initial_params)

            assert optimized_params is not None
            assert min_energy == -1.5

    def test_get_iteration_count(self, vqe_instance: VQEAlgorithm) -> None:
              """Test iteration count retrieval."""
              with patch.object(vqe_instance, 'get_iteration_count', return_value=100):
                            count = vqe_instance.get_iteration_count()
                            assert count == 100

          def test_num_qubits_validation(self) -> None:
                    """Test that invalid number of qubits raises error."""
                    with pytest.raises((ValueError, TypeError)):
                                  VQEAlgorithm(num_qubits=0, num_layers=1)

                def test_num_layers_validation(self) -> None:
                          """Test that invalid number of layers raises error."""
                          with pytest.raises((ValueError, TypeError)):
                                        VQEAlgorithm(num_qubits=2, num_layers=0)

                      @pytest.mark.parametrize("num_qubits,num_layers", [
                                (2, 1),
                                (3, 2),
                                (4, 3),
                                (6, 2),
                      ])
    def test_various_qubit_configurations(self, num_qubits: int, num_layers: int) -> None:
              """Test VQEAlgorithm with various qubit configurations."""
              vqe = VQEAlgorithm(num_qubits=num_qubits, num_layers=num_layers)
              assert vqe.num_qubits == num_qubits
              assert vqe.num_layers == num_layers
      
