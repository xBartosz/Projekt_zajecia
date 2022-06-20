import platform
import sys
import os
import timeit
from multiprocessing import Pool
from statistics import median
from concurrent.futures import ThreadPoolExecutor


def suma(n):

    for i in range(1, n+1):
        (n - i) * i


# Utworzona funkcja liczy sume, podaną w treści zadania


liczby = [15972490, 80247910, 92031257, 75940266, 97986012,
          87599664, 75231321, 11138524, 68870499, 11872796,
          79132533, 40649382, 63886074, 53146293, 36914087,
          62770938]


listaproc4 = []
listaprocdost = []
listawat1 = []
listawat4 = []


# wypisanie liczb z treści zadania
# utworzenie list do których zostaną dodane zmierzone czasy


def procesy4():
    with Pool(processes=4) as pool:
        pool.map(suma, liczby)


def procesydost():
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(suma, liczby)


def watek1():
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(suma, liczby)


def watki4():
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(suma, liczby)

# Utworzenie funkcji dla 4procesów, liczby procesów dostępnych w systemie,
# dla jednego wątku oraz dla czterech wątków
# Następnie wysłanie argumentów z listy 'liczby' do funkcji 'suma'


def main():
    for i in range(5):
        listawat1.append(timeit.timeit(stmt='watek1()',
                                       number=1, globals=globals()))

        listawat4.append(timeit.timeit(stmt='watki4()',
                                       number=1, globals=globals()))

        listaproc4.append(timeit.timeit(stmt='procesy4()',
                                        number=1, globals=globals()))

        listaprocdost.append(timeit.timeit(stmt='procesydost()',
                                           number=1, globals=globals()))

# Utworzenie funkcji, która ma za zadanie zmierzyć czas danych funkcji
# po jednym razie (5 razy)


if __name__ == '__main__':
    main()

# Wywołanie funkcji pomiaru czasu

    raport = '''
     <html>
     <head>
        <title> Raport - Bartosz Fiet </title>
        <style>

        table {
            border-collapse: collapse;
            width: 100%;
            font-family: arial
            }

        table th{
            text-align:center;
            background-color:#C0C0C0;
            padding: 7px;
        }

        table td {
            border:1px solid grey;
            text-align:center;
            padding:7px;
        }

        table tr:nth-child(odd) td{
            background-color:#E0E0E0;
        }
        </style>
     </head>
          <body>
    <b><h1>Multithreading/Multiprocessing benchmark results</h1>
    </br>
    <h2>Execution environment</h2></b>
    <p>Python version: ''' + platform.python_version() + ''' </br>
         Interpreter: ''' + platform.python_implementation() + '''   </br>
         Interpreter version: ''' + sys.version + '''  </br>
         Operating system: ''' + platform.system() + '''    </br>
         Operating system version: ''' + platform.release() + '''  </br>
         Processor: ''' + platform.processor() + ''' </br>
         CPUs: ''' + str(os.cpu_count()) + '''    </br>
    </p>
    </br>
    <b><h2>Test results</h2></b>
    </br>
    <p>The following table shows detailed test results:</p>



            <table>
            <tr>
                <th>Execution:</th>
                <th>1 thread (s)</th>
                <th>4 thread (s)</th>
                <th>4 processes (s)</th>
                <th>processes based on number of CPUs (s)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>''' + str("%.2f" % listawat1[0]) + '''</td>
                <td>''' + str("%.2f" % listawat4[0]) + '''</td>
                <td>''' + str("%.2f" % listaproc4[0]) + '''</td>
                <td>''' + str("%.2f" % listaprocdost[0]) + '''</td>
            </tr>
            <tr>
                <td>2</td>
                <td>''' + str("%.2f" % listawat1[1]) + '''</td>
                <td>''' + str("%.2f" % listawat4[1]) + '''</td>
                <td>''' + str("%.2f" % listaproc4[1]) + '''</td>
                <td>''' + str("%.2f" % listaprocdost[1]) + '''</td>
            </tr>
            <tr>
                <td>3</td>
                <td>''' + str("%.2f" % listawat1[2]) + '''</td>
                <td>''' + str("%.2f" % listawat4[2]) + '''</td>
                <td>''' + str("%.2f" % listaproc4[2]) + '''</td>
                <td>''' + str("%.2f" % listaprocdost[2]) + '''</td>
            </tr>
            <tr>
                <td>4</td>
                <td>''' + str("%.2f" % listawat1[3]) + '''</td>
                <td>''' + str("%.2f" % listawat4[3]) + '''</td>
                <td>''' + str("%.2f" % listaproc4[3]) + '''</td>
                <td>''' + str("%.2f" % listaprocdost[3]) + '''</td>
            </tr>
            <tr>
                <td>5</td>
                <td>''' + str("%.2f" % listawat1[4]) + '''</td>
                <td>''' + str("%.2f" % listawat4[4]) + '''</td>
                <td>''' + str("%.2f" % listaproc4[4]) + '''</td>
                <td>''' + str("%.2f" % listaprocdost[4]) + '''</td>
            </tr>
            </table>
    <b><h2>Summary</h2></b>
    <p>The following table shows the median of all results:</p>
            <table>

            <tr>
                <th>Execution:</th>
                <th>1 thread (s)</th>
                <th>4 thread (s)</th>
                <th>4 processes (s)</th>
                <th>processes based on number of CPUs (s)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>''' + str("%.2f" % median(listawat1)) + '''</td>
                <td>''' + str("%.2f" % median(listawat4)) + '''</td>
                <td>''' + str("%.2f" % median(listaproc4)) + '''</td>
                <td>''' + str("%.2f" % median(listaprocdost)) + '''</td>
            </tr>

            </table>
    <p>App author: Bartosz Fiet</p>


            </body>
        </html>
        '''

    with open('html2_report.html', 'w') as f:
        f.write(raport)


# Utworzenie strony zwracającej dane systemowe, oraz czasy pomiarów
# Zapisanie utworzonego raportu(strony) do pliku
