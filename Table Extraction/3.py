# EXTRACT ALL TABLES FROM A PDF FILE

import tabula

# URL
# pdf_path = "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0JtQW1MX2VMSi1KR1FoeWdEQUN3VURWLXdDUXxBQ3Jtc0trUFlILTZIT1pWZVhjSjdKM2JYdUJid3NSVmZISTJsT0h5TmpXNTZDRjVFSEpPUXdPYllYQVhySWptMU02YS1UZkJnVHl0RFl3bHgtcU5GQmoyODVLN1BoTHdTbFEtTm5pMXZ0ZUNpZVFIYzQzdy1iSQ&q=https%3A%2F%2Fsedl.org%2Fafterschool%2Ftoolkits%2Fscience%2Fpdf%2Fast_sci_data_tables_sample.pdf&v=tEFAFQXaOWw"
pdf_path = "demoPDF.pdf"

dfs = tabula.read_pdf(pdf_path, pages='all')

for i in range(len(dfs)):
    dfs[i].to_csv(f"Table{i}.csv")
    print(f"Table{i}")