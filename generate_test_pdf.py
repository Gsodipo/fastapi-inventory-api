from fpdf import FPDF
import subprocess
import sys

# Run tests and capture ALL output (stdout + stderr)
result = subprocess.run(
    [sys.executable, "-m", "pytest", "test_app.py", "-v"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Unit Test Results", ln=True)

pdf.set_font("Courier", size=10)
pdf.multi_cell(0, 8, result.stdout)

# Save PDF
pdf.output("unit_test_results.pdf")
print("PDF generated with test results!")
