# coding=utf-8

import matplotlib.pyplot as p
import random
import timeit

# https://github.com/luscafter/cana
# Teste o software na ferramenta Colab:
# https://colab.research.google.com

# Função responsável pelo algoritmo Counting Sort

def counting_sort(v):
    n = len(v)
    bigger = max(v)
    output = [0] * n
    count = [0] * (bigger + 1)

    for i in range(n):
        count[v[i]] += 1

    for i in range(1, bigger + 1):
        count[i] += count[i - 1]

    for i in range(n):
        output[count[v[i]] - 1] = v[i]
        count[v[i]] -= 1

    for i in range(n):
        v[i] = output[i]

    return v

# Função responsável pelo algoritmo Radix Sort

def radix_sort(v):
	exp = 1
	n = len(v)
	bigger = max(v)
	output = [0] * n
	
	while (bigger / exp) > 0:
		count = [0] * 10

		for i in range(n):
			count[(v[i] // exp) % 10] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		for i in range(n - 1, -1, -1):
			count[(v[i] // exp) % 10] -= 1
			output[count[(v[i] // exp) % 10]] = v[i]

		for i in range(n):
			v[i] = output[i]

		exp *= 10

	return v

# Função responsável pelo algoritmo Bucket Sort

def bucket_sort(v):
	n = len(v)
	size = max(v) / n

	buckets = []

	for i in range(n):
		buckets.append([]) 

	for i in range(n):
		j = int(v[i] / size)

		if j != n:
			buckets[j].append(v[i])
		else:
			buckets[n - 1].append(v[i])

	# Classifica os elementos dentro dos intervalos usando o método do Insertion Sort

	for i in range(n):
		insertion_sort(buckets[i])
            
	output = []

	for i in range(n):
		output += buckets[i]

	return v

# Função responsável por classificar os elementos da função bucket_sort()

def insertion_sort(v):
	for i in range (1, len(v)):
		k = v[i]
		j = i - 1

		while (j >= 0 and k < v[j]):
			v[j + 1] = v[j]
			j -= 1

		v[j + 1] = k

def shell_sort(v):
	exp = 1
	n = len(v)

	while exp > 0:
		for i in range(exp, n):
			k = v[i]
			j = i

			while j >= exp and k < v[j - exp]:
				v[j] = v[j - exp]
				j -= exp
				v[j] = k

		exp = int(exp / 2.2)

	return v

# Função responsável por gerar um vetor com valores aleatórios

def randomize(n):
	v = []
	random.seed()

	for i in range(n):
		v.append(random.randint(1, n))

	return v

# Função responsável por executar a função de preencher e ordenar o vetor

def fill(function, name):
	print("\nExecutando [{}]\n".format(name))

	for i in size:
		print("[+] Preenchendo e ordenando vetor de tamanho [{}]".format(i))
		v = randomize(i)
		copy = list(v)
		times.append(timeit.timeit(function.format(copy), setup="from __main__ import " + name, number=1))

		if i == 24000:
			print()

size = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
functions = ["counting_sort({})", "radix_sort({})", "bucket_sort({})", "shell_sort({})"]
names = ["counting_sort", "radix_sort", "bucket_sort", "shell_sort"]

# Função responsável por plotar os gráficos das funções

for i in range(4):
	times = []
	fill(functions[i], names[i])
	fig, ax = p.subplots()
	text = "Counting Sort"

	if i == 1:
		text = "Radix Sort"
	elif i == 2:
		text = "Bucket Sort"
	elif i == 3:
		text = "Shell Sort"

	ax.plot(size, times, label=text)

	p.ylabel("TEMPO")
	p.xlabel("TAMANHO")
	p.title("Algoritmos lineares")

	legend = ax.legend(loc="upper center", shadow=True)

	frame = legend.get_frame()
	frame.set_facecolor('1.0')

	for label in legend.get_texts():
		label.set_fontsize('large')

	for label in legend.get_lines():
		label.set_linewidth(2.0)

	p.show()
