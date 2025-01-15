
# **Cppcheck Syntax Checker**

## **Description**
This Python script checks the syntax and potential issues in C/C++ source files using `cppcheck`. It traverses a specified directory and all its subdirectories, running `cppcheck` on each C/C++ file it finds. The results are saved in an HTML report.

---

## **How It Works**
1. The script uses the `subprocess` module to run `cppcheck` on each file with relevant extensions.
2. It generates an HTML report (`output.html`) with detailed findings, highlighting any issues discovered in the code.
3. The script also removes all `__pycache__` directories after processing to keep the workspace clean, with specific handling based on the operating system.

---

## **Setting Up the Environment**

### **Adding Cppcheck to Your PATH Temporarily**
To ensure the script can execute `cppcheck` from any location, you might need to add `cppcheck` to your system's `PATH` temporarily:

1. **Export the PATH**: Open a terminal and run the following command to add the `cppcheck` directory to your `PATH`:
   ```bash
   export PATH=$PATH:/folder/path
   ```
   Replace `/folder/path` with the actual path to the `cppcheck` binary.

2. **Use an Alias (If Necessary)**: If the above step doesn’t work, you can create an alias for `cppcheck`:
   - Open your `.bashrc` file:
     ```bash
     vi ~/.bashrc
     ```
   - Add the following line at the end of the file:
     ```bash
     alias cppcheck='/app/Siemens/b/.p/pedro/larissaBarc/src/barc/cppcheck-2.12.1/cppcheck'
     ```
   - Save and close the file by pressing `ESC` and typing `:x`.

3. **Refresh Your Configurations**: After editing `.bashrc`, run the following command to apply the changes:
   ```bash
   source ~/.bashrc
   ```

---

## **Usage**

### **Run the Script**
1. Make sure Python and `cppcheck` are installed and properly configured in your `PATH`.
2. Place the script in the directory you wish to analyze.
3. Execute the script using Python:
   ```bash
   python script_name.py
   ```

### **Output**
The script generates an `output.html` file in the same directory, containing a comprehensive report of the `cppcheck` analysis.

---

## **Requirements**
- Python 3.x
- `cppcheck` installed on your system
