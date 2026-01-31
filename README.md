Day 1

Learned the basics of Python’s os module.
Explored common OS-level commands and their parameters.
Got a basic understanding of how a shell works and how it communicates with the kernel.
Used core functions like os.mkdir(), os.remove(), os.getcwd(), etc.

Day 2

Built a very basic working shell.
Implemented simple commands like open, exit, make folder, delete folder, and cd.
Spent time experimenting with different logic paths and custom wording for commands.

Day 3

Shell reached a usable stage with core features:

Create/delete folders
Create/delete files
Navigate inside folders
Go back to parent directory
List directories
Sleep and exit commands
Clear screen
Also experimented with UX improvements:
Emoji support in messages
Folder created/deleted status messages
Typing animation effect
Colored text output

Day 4

Refactored command-handling logic for better readability.
Separated command parsing from execution logic.
Improved error handling for invalid commands and missing paths.

Day 5

Added command history tracking.
Implemented basic in-memory storage for previously executed commands.
Improved user feedback when repeating or mistyping commands.

Day 6

Worked on directory navigation stability.
Handled edge cases like invalid cd paths and restricted directories.
Ensured shell doesn’t crash on incorrect inputs.

Day 7

Focused on modular architecture.
Started separating file operations, navigation logic, and UI output into different modules.
Prepared the base structure for future extensibility.

Day 8

Improved output formatting and readability.
Enhanced colored text handling for success, error, and info messages.
Fine-tuned typing animation speed for better UX.

Day 9

Optimized file and folder operations for consistency.
Ensured clear feedback for every operation (create, delete, navigate).
Reduced repetitive code using helper functions.

Day 10

Worked on shell stability and flow.
Tested continuous command execution without restarting the shell.
Fixed minor bugs related to directory state management.

Day 11

Started planning the transition from CLI to GUI-based terminal.
Researched how command logic can remain backend-driven while UI changes.
Adjusted architecture to keep core logic UI-independent.

Day 12

Improved command parsing logic to support flexible input formats.
Enhanced error messages to be more user-friendly and descriptive.
Focused on making the shell feel more “human” and interactive.

Day 13

Stress-tested shell with repeated operations and incorrect inputs.
Ensured graceful handling of failures without breaking execution flow.
Polished command history behavior.

Day 14

Cleaned up codebase and added inline documentation.
Reviewed overall system flow from input → parsing → execution → output.
Prepared project for public sharing and further expansion.

Day 15

Final review of features and architecture.
Validated modular design for future GUI integration.
Documented learnings around OS interaction, system-level programming, and shell behavior.
Project reached a stable baseline ready for real-world system-level experimentation.
