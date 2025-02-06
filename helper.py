import pandas as pd
import csv

def read_csv_autodelim(filelike):
    # Erstmal an den Anfang des Streams springen
    filelike.seek(0)
    # Kleine Stichprobe einlesen (z.B. 2048 Byte) und in String umwandeln
    sample_bytes = filelike.read(2048)
    sample_text = sample_bytes.decode('utf-8', errors='replace')
    
    # Wieder an den Anfang, damit pd.read_csv alles bekommt
    filelike.seek(0)
    
    # csv.Sniffer mit möglichen Trennzeichen
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample_text, delimiters=[',', ';'])
    
    # Jetzt mit dem ermittelten delimiter
    df = pd.read_csv(filelike, delimiter=dialect.delimiter)
    
    return df
