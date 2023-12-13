import tkinter as tk

class DNATranslator:
    CODON_TABLE = {
         'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
            'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence.upper()

    def transcribe_to_rna(self):
        return self.dna_sequence.replace('T', 'U')

    def translate_to_protein(self):
        rna_sequence = self.transcribe_to_rna()
        protein_sequence = ''
        for i in range(0, len(rna_sequence), 3):
            codon = rna_sequence[i:i + 3]
            if len(codon) == 3:
                protein_sequence += self.CODON_TABLE.get(codon, 'X')  # 'X' untuk kodon yang tidak diketahui
        return protein_sequence

class DNAConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Penerjemah DNA")

        self.label = tk.Label(root, text="Masukkan Urutan DNA:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.translate_button = tk.Button(root, text="Terjemahkan", command=self.translate_sequence)
        self.translate_button.pack()

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def translate_sequence(self):
        sequence = self.entry.get()
        translator = DNATranslator(sequence)

        rna_result = translator.transcribe_to_rna()
        protein_result = translator.translate_to_protein()

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Urutan RNA:\n{rna_result}\n\nUrutan Protein:\n{protein_result}")

def run_app():
    root = tk.Tk()
    app = DNAConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()