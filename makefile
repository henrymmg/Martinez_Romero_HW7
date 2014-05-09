all : datos_iniciales.txt datos_finales.txt
	python animacion_eq_onda_1D_cuerda.py
datos_cuerda.dat : cuerda_wave_equation_1D.x
	./cuerda_wave_equation_1D.x
a.out : cuerda_wave_equation_1D.c
	cc cuerda_wave_equation_1D.c -o cuerda_wave_equation_1D.x -lm
clean :
	rm *.txt *.x iniciales.png