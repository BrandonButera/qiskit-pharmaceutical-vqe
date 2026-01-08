# Contributing to qiskit-pharmaceutical-vqe

We welcome contributions to the Quantum VQE for Pharmaceutical Applications project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive environment for all contributors.

## Getting Started

1. Fork the repository on GitHub
2. 2. Clone your fork locally:
   3.    ```bash
            git clone https://github.com/YOUR_USERNAME/qiskit-pharmaceutical-vqe.git
            cd qiskit-pharmaceutical-vqe
            ```

         3. Create a virtual environment:
         4.    ```bash
                  python -m venv venv
                  source venv/bin/activate  # On Windows: venv\Scripts\activate
                  ```

               4. Install development dependencies:
               5.    ```bash
                        pip install -e ".[dev]"
                        pre-commit install
                        ```

                     ## Development Workflow

                 ### Making Changes

           1. Create a new branch for your feature or bugfix:
           2.    ```bash
                    git checkout -b feature/your-feature-name
                    ```

                 2. Make your changes and commit them:
                 3.    ```bash
                          git add .
                          git commit -m "Description of your changes"
                          ```

                       3. Ensure your code follows the style guidelines:
                       4.    - Run Black for code formatting: `black pharma_vqe tests`
                             -    - Run isort for import sorting: `isort pharma_vqe tests`
                                  -    - Check with flake8: `flake8 pharma_vqe tests`
                                       -    - Type check with mypy: `mypy pharma_vqe`
                                        
                                            - ### Running Tests
                                        
                                            - Run the test suite to ensure your changes work correctly:
                                        
                                            - ```bash
                                              pytest
                                              pytest --cov=pharma_vqe  # With coverage report
                                              ```

                                              ### Documentation

                                              - Add docstrings to all functions and classes using Google-style docstrings
                                              - - Update README.md if adding new features
                                                - - Update CHANGELOG.md with your changes
                                                 
                                                  - ## Submitting Changes
                                                 
                                                  - 1. Push your branch to GitHub:
                                                    2.    ```bash
                                                             git push origin feature/your-feature-name
                                                             ```

                                                          2. Create a Pull Request (PR) on GitHub with a clear description:
                                                          3.    - Reference any related issues
                                                                -    - Describe what changes you made and why
                                                                     -    - Include any relevant test results
                                                                      
                                                                          - 3. Your PR will be reviewed by maintainers. Be prepared to address feedback.
                                                                           
                                                                            4. ## Pull Request Guidelines
                                                                           
                                                                            5. - Include tests for new features
                                                                               - - Update documentation as needed
                                                                                 - - Ensure all tests pass (`pytest`)
                                                                                   - - Maintain or improve code coverage
                                                                                     - - Follow PEP 8 and black formatting standards
                                                                                       - - Add meaningful commit messages
                                                                                        
                                                                                         - ## Reporting Issues
                                                                                        
                                                                                         - When reporting issues, please include:
                                                                                         - - A clear description of the problem
                                                                                           - - Steps to reproduce the issue
                                                                                             - - Expected vs actual behavior
                                                                                               - - Python version and environment details
                                                                                                 - - Relevant code snippets or error messages
                                                                                                  
                                                                                                   - ## Questions?
                                                                                                  
                                                                                                   - Feel free to open an issue to ask questions or discuss improvements to the project.
                                                                                                  
                                                                                                   - ## License
                                                                                                  
                                                                                                   - By contributing to this project, you agree that your contributions will be licensed under the same Apache-2.0 license as the project.
                                                                                                  
                                                                                                   - Thank you for contributing!
                                                                                                   - 
