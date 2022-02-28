import sqlite3

def line(length):
    print('-'*length)

def create_table():
    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE codons (
        codon TEXT, 
        acronym TEXT, 
        protein TEXT
    )''')
    conn.commit()
    conn.close()

def add_codon(cdn, acr, ptn):
    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()
    c.execute('INSERT INTO codons VALUES (?,?,?)', 
    (cdn, acr, ptn))
    conn.commit()
    conn.close()

def del_codon(id):
    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()
    c.execute('DELETE from codons WHERE rowid = ?', id)
    conn.commit()
    conn.close()
