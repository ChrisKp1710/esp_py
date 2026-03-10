# Appunti su input e output in Python per principianti
# Input: dati che l'UTENTE inserisce (da tastiera)
# Output: dati che il programma MOSTRA (sullo schermo)

# ============================================================
# PARTE 1: ESEMPI SEMPLICI E FACILI
# ============================================================

print("=== ESEMPIO 1: OUTPUT SEMPLICE ===")
# Il modo più semplice: print() mostra testo sullo schermo
print("Ciao!")
print("Questo è Python!")

print("\n=== ESEMPIO 2: INPUT SEMPLICE ===")
# Il modo più semplice: input() chiede all'utente di scrivere
nome = input("Come ti chiami? ")
# Poi mostriamo quello che l'utente ha inserito
print("Ciao", nome, "!")

# ============================================================
# PARTE 2: CAPIRE COME FUNZIONANO
# ============================================================

print("\n=== COME FUNZIONA INPUT ===")
# Quando usi input(), il programma si ferma e aspetta l'utente
# L'utente scrive qualcosa e preme Invio
# Quello che l'utente scrive VIENE SALVATO nella variabile
# ATTENZIONE: input() restituisce sempre una stringa (testo), non un numero!

numero_testo = input("Scrivi un numero: ")
print("Hai scritto:", numero_testo)
print("Tipo di dato:", type(numero_testo))  # Mostra: <class 'str'> cioè stringa!

print("\n=== COME CONVERTIRE A NUMERO ===")
# Se voglio usare il numero per fare calcoli, devo convertirlo con int()
numero_vero = int(input("Scrivi un altro numero: "))
print("Hai scritto:", numero_vero)
print("Tipo di dato:", type(numero_vero))  # Mostra: <class 'int'> cioè numero!
risultato = numero_vero + 10
print("Numero + 10 =", risultato)

print("\n=== COME FUNZIONA OUTPUT ===")
# print() mostra dati sullo schermo
# Puoi stampare stringhe, numeri, risultati di operazioni
print("Una stringa:", "Ciao!")
print("Un numero:", 42)
print("Un'operazione:", 5 + 3)

# ============================================================
# PARTE 3: ESEMPI PIÙ COMPLESSI
# ============================================================

print("\n=== ESEMPIO COMPLETO: CALCOLO ETÀ ===")
# Raccogliamo due input: anno di nascita e anno corrente
anno_nascita = int(input("In che anno sei nato? "))
anno_corrente = 2023
# Calcoliamo l'età
eta = anno_corrente - anno_nascita
# Mostriamo il risultato
print("Hai circa", eta, "anni!")

print("\n=== ESEMPIO: CONCATENAZIONE ===")
# Possiamo unire stringhe da input con output personalizzato
colore = input("Quale è il tuo colore preferito? ")
animale = input("Quale è il tuo animale preferito? ")
# Creiamo una frase personalizzata
frase = "Mi piace il colore " + colore + " e l'animale " + animale
print(frase)

print("\n=== ESEMPIO: CONDIZIONI CON INPUT ===")
# Possiamo usare input() dentro una condizione
numero_segreto = 7
numero_utente = int(input("Indovina il numero (1-10): "))
if numero_utente == numero_segreto:
    print("Esatto! Hai vinto!")
else:
    print("Sbagliato! Il numero era:", numero_segreto)

# ============================================================
# RIASSUNTO E ERRORI COMUNI
# ============================================================

print("\n=== ERRORI COMUNI ===")
# Errore 1: Usare input() come numero senza convertire
# numero = input("Numero: ")
# risultato = numero + 10  # ERRORE! Puoi't sommare stringa e numero
# SOLUZIONE: numero = int(input("Numero: ")) oppure numero = int(numero)

# Errore 2: Dimenticare le virgolette in print()
# print(Ciao)  # ERRORE! Non sa cosa sia Ciao
# SOLUZIONE: print("Ciao")

# Errore 3: Mescolare input e stampa senza logica
# L'applicazione sarà confusa se non organizzi bene input e output

print("\n=== RIASSUNTO FINALE ===")
print("1. print() → OUTPUT (mostra sullo schermo)")
print("2. input() → INPUT (prende dati da tastiera)")
print("3. input() restituisce SEMPRE una STRINGA")
print("4. Usa int() per convertire a numero intero")
print("5. Usa float() per convertire a numero decimale")