# EXTRACT SINGLE TABLE FROM A "PARTIULAR PDF PAGE"

import tabula

# URL
# pdf_path = "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0JtQW1MX2VMSi1KR1FoeWdEQUN3VURWLXdDUXxBQ3Jtc0trUFlILTZIT1pWZVhjSjdKM2JYdUJid3NSVmZISTJsT0h5TmpXNTZDRjVFSEpPUXdPYllYQVhySWptMU02YS1UZkJnVHl0RFl3bHgtcU5GQmoyODVLN1BoTHdTbFEtTm5pMXZ0ZUNpZVFIYzQzdy1iSQ&q=https%3A%2F%2Fsedl.org%2Fafterschool%2Ftoolkits%2Fscience%2Fpdf%2Fast_sci_data_tables_sample.pdf&v=tEFAFQXaOWw"
pdf_path = "demoPDF.pdf"

dfs = tabula.read_pdf(pdf_path, pages=1)

# Checking Number of Tables in that particular page
print(len(dfs))

# Printing the Table
print(dfs[0])

# Writing the Table to a CSV
dfs[0].to_csv("Table1.csv")

# OR ----------------------------------------------- (recommended)

tabula.convert_into(pdf_path, "Table2.csv", output_format="csv", pages=1)