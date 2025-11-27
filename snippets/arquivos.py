def ler_arquivo(c): return open(c,'r',encoding='utf-8').read()

def escrever_arquivo(c,t): open(c,'w',encoding='utf-8').write(t)