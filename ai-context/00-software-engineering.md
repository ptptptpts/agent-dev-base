# General Software Engineering Guidelines

## Development Process (TDD Flow)
You must follow the **Test-Driven Development (TDD)** process for every new feature or bug fix:
1. **Test Implementation**: Write comprehensive test cases based on the requirements defined in the issue/goal **before** writing any application logic.
2. **Verification of Failure**: Ensure the new tests fail in the current environment (Red phase).
3. **Minimal Implementation**: Write the minimal amount of code necessary to make the tests pass (Green phase).
4. **Regression Testing**: You **must** ensure that **all existing tests pass** alongside the new ones. Do not break existing functionality.
5. **Refactor**: Clean up the code while keeping all tests passing.

## Modularity & Separation of Concerns (SoC)
To ensure maintainability and prevent regression, code must be decoupled and modularized:
1. **Layered Architecture**: Strictly separate code into **Engine/Data**, **Logic/Domain**, and **UI/Interface** layers. Each layer must only communicate with adjacent layers via well-defined interfaces.
2. **High Cohesion & Low Coupling**: Modules should be highly focused on a single responsibility. Changes in one module must have zero to minimal impact on unrelated modules.
3. **Abstraction over Implementation**: Depend on abstractions (interfaces) rather than concrete implementations to allow easy swapping and testing of components.
4. **Encapsulation**: Keep internal module logic private. Only expose what is absolutely necessary for other modules to function.

## Surgical Modifications & Minimal Impact
- **Targeted Changes**: When resolving an issue, only modify the specific lines or functions directly related to the task. 
- **Side Effect Prevention**: Always analyze the recursive impact of a change. If a modification affects multiple modules, consider if the modules are too tightly coupled and refactor if necessary.
- **YAGNI (You Ain't Gonna Need It)**: Do not add extra functionality or layers "just in case." Keep the codebase as small and efficient as possible.

## Architectural Principles
- **SOLID**: Follow SOLID principles for robust object-oriented or functional design.
- **Clean Code**: Meaningful variable names, small functions, no side effects.
- **DRY (Don't Repeat Yourself)**: Extract common logic into reusable modules.
