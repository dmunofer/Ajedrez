def ajedrez(filename):

    tablero_inicial= '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero = []

    for e in tablero_inicial.split('\n'):
        tablero.append(e.split('\t'))

    f = open(filename,'w')
    for e in tablero:
        f.write('\t'.join(e)+'\n')
    f.close()

    movimientos = 0
    while True:
        continua = input('Quieres hacer otro movimiento (si/no) : ')
        if continua == 'si':
            fila_origen = int(input('Introduce la fila de la pieza: '))
            columna_origen = int(input('Introduce la columna de la pieza: '))
            fila_destino = int(input('Introduce la fila destino: '))
            columna_destino = int(input('Introduce la columna destino: '))
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_origen-1][columna_origen-1]
            tablero[fila_origen-1][columna_origen-1] = ' '
            movimientos+=1
            f=open(filename,'w')
            f.write('Movimiento'+ f'{movimientos}' + '\n')
        else:
            break

            for e in tablero:
                f.write('\t'.join(e)+'\n')
            f.close()

