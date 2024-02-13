# Modeling-in-Nature-Science

## Prologo

## Introduction
El estudio del movimiento browniano proporciona un punto de partida fundamental para abordar diversas aplicaciones en la física, especialmente en el contexto de sistemas microscópicos. La comprensión del movimiento errático de partículas coloidales impulsadas por el caos térmico del entorno ha llevado a la exploración de técnicas como el potencial de ratchet para dirigir dicho movimiento de manera controlada. A medida que se profundiza en estas dinámicas, surge la posibilidad de aplicar estos conocimientos en la separación de iones, un área crucial para el tratamiento del agua y la extracción de recursos valiosos de fuentes abundantes como el agua de mar. Además, este estudio se proyecta más allá, abarcando la modelación de fenómenos complejos como la propagación de enfermedades, utilizando conceptos de movimiento browniano y procesos de Markov. Asimismo, se expande hacia la simulación de la dispersión de contaminantes en la atmósfera, aplicando principios estocásticos lagrangianos. Esta progresión lógica desde el estudio del movimiento browniano hasta aplicaciones prácticas en campos tan diversos resalta la versatilidad y relevancia de este enfoque en la investigación física.

## Fundamento teorico
En este trabajo, exploramos la intersección entre la física y las matemáticas aplicadas, abordando desde procesos estocásticos y movimiento browniano hasta ecuaciones Langevin y Fokker-Planck. Utilizamos estas herramientas para estudiar fenómenos como la propagación de enfermedades y la dispersión de contaminantes atmosféricos, ofreciendo un enfoque unificado para comprender y predecir eventos relevantes en escalas micro y macroscópicas.

### Procesos estocásticos y de Markov
Un proceso estocástico es un modelo matemático que describe la evolución temporal de un sistema incorporando la incertidumbre mediante variables aleatorias. Matemáticamente, se expresa como $X(t)$, donde $t$ es el tiempo y $X(t)$ es una variable aleatoria que representa el estado del sistema en el instante $t$. En este contexto, un proceso de Markov es un tipo específico de proceso estocástico caracterizado por la propiedad de Markov, donde la probabilidad futura $P(X(t + \Delta t) | X(t))$ depende exclusivamente del estado presente $X(t)$ y no del historial completo del sistema. Esta propiedad se formula mediante la ecuación de Chapman-Kolmogorov, que describe cómo evoluciona la probabilidad condicional a lo largo del tiempo. La simplificación inherente de la dependencia temporal en los procesos de Markov los hace especialmente útiles en la simulación de fenómenos donde el estado actual es suficiente para prever el futuro, como en modelos epidemiológicos, teoría de colas y diversos problemas en finanzas y ciencias aplicadas.

### Ecuaciòn de Langevin y Focker-Planck
La ecuación de Langevin describe la evolución temporal de una partícula en un medio fluido, incorporando términos deterministas y estocásticos. Matemáticamente, se expresa como 
$$m\frac{dv}{dt} = -\gamma v + \sqrt{2k_BT\gamma}\xi(t)$$
, donde \(m\) es la masa de la partícula, \(v\) es su velocidad, \(\gamma\) es el coeficiente de fricción, \(k_B\) es la constante de Boltzmann, \(T\) es la temperatura, y \(\xi(t)\) es un término de ruido blanco gaussiano.

La ecuación de Fokker-Planck describe la evolución de la probabilidad de encontrar una partícula en un determinado estado en función del tiempo. Para el caso de la ecuación de Langevin, toma la forma de una ecuación diferencial parcial, expresada como 
$$\frac{\partial P}{\partial t} = -\frac{\partial}{\partial v}(A P) + \frac{\partial^2}{\partial v^2}(B P)
$$
, donde \(P\) es la función de densidad de probabilidad y \(A\) y \(B\) son funciones asociadas con los términos deterministas y estocásticos de la ecuación de Langevin, respectivamente.

### Motor Browniano
Los motores brownianos son sistemas microscópicos en los que las partículas o moléculas experimentan un movimiento dirigido debido a la asimetría en su entorno. Este movimiento dirigido surge de la combinación de fluctuaciones térmicas aleatorias y un sesgo sistemático, a menudo inducido por fuerzas externas o paisajes de potenciales. Los motores brownianos se han estudiado en diversos contextos, como en el movimiento de motores moleculares dentro de células biológicas o en el transporte de partículas coloidales en entornos no uniformes. Comprender y manipular el movimiento browniano es crucial para aplicaciones en nanotecnología, donde estos motores pueden ser aprovechados para tareas como la administración controlada de medicamentos, la clasificación de partículas o la alimentación de máquinas a escala nanométrica.

$$m\dot{x} = -\frac{dV}{dx} +\frac{1}{m\gamma}F + \sqrt{2D}\xi(t)$$
$$V:\text{Potential ratchet}$$

    
$$V(x)=V_0 \left[C+ \sin \left(2 \pi (x-x_0)  \right) +\frac{1}{4} \sin \left(4 \pi (x-x_0) \right) \right]$$


$$C\approx -1.1 \quad x_0 \approx -1.9$$

### Modelos epidemicos
Los modelos epidemiológicos son esenciales para comprender y gestionar la propagación de enfermedades en poblaciones. Entre ellos, destaca el modelo SIR, que divide a los individuos en las categorías Susceptibles (S), Infectados (I) y Recuperados (R), utilizando ecuaciones diferenciales para modelar las transiciones entre estas categorías. Este enfoque se emplea para simular y predecir el curso de una enfermedad, permitiendo evaluar estrategias de control. Más ampliamente, el término "modelo epidemiológico" abarca diversos enfoques matemáticos y computacionales utilizados para estudiar la distribución y determinantes de enfermedades en poblaciones. Estos modelos son herramientas fundamentales en la salud pública, analizando patrones de enfermedad, identificando factores de riesgo y diseñando estrategias efectivas para la prevención y el control de enfermedades a nivel poblacional.

$$S+I+R=N$$
<!--
$$\begin{align}
\frac{dS}{dt}&=-\frac{\beta}{N}SI\\
\frac{dI}{dt}&=\frac{\beta}{N}SI-\gamma I\\
\frac{dR}{dt}&=\gamma I
\end{align}$$
-->

Ecuación diferencial con población variable.

$$\begin{align}
\frac{dS}{dt}&=-\frac{\beta}{N}SI-\phi S + \eta N\\
\frac{dI}{dt}&=\frac{\beta}{N}SI-(\gamma+\phi) I\\
\frac{dR}{dt}&=\gamma I (1-\lambda) - \phi R
\end{align}$$

Version estocastico del modelo SIR con población variable (falta modificar, e colocado el tradicional).

$$Prob\{\Delta S (t)=i,\Delta I(t)=j|(S(t),I(t))\}=
	\begin{cases}
		\frac{\beta}{N} S(t)I(t)\Delta t+o(\Delta t),&(i,j)=(-1,1)(infección)\\
		\gamma I(t)\Delta + o(\Delta t),&(i,j)=(0,-1)(recuperación)\\
		1-\Big[ \frac{\beta}{N}S(t)I(t)+\gamma I(t) \Big]\Delta t,&(i,j)=(0,0)\\
		o(\Delta t),& otherwise 	
	\end{cases}$$

Los parametros $\eta, \gamma, \beta, \lambda$ se fijan de acuerdo a fuentes oficiales o a travez del ajuste con los datos.

### Procesos Metereologicos
La meteorología, como disciplina científica dedicada al estudio de la atmósfera terrestre, juega un papel crucial en la comprensión de los patrones climáticos y en la formulación de modelos para evaluar la dispersión de contaminantes en el aire. Implica la observación y análisis de diversas variables atmosféricas, utilizando herramientas como estaciones meteorológicas y satélites. En este contexto, los Modelos Estocásticos Lagrangianos de Partículas (SLPM) destacan al seguir la trayectoria de partículas virtuales bajo influencia meteorológica. Estos modelos, al incorporar elementos estocásticos, capturan la variabilidad inherente en la dispersión atmosférica, considerando factores como la velocidad del viento y turbulencias. Su aplicabilidad en la modelación de la calidad del aire brinda detalles precisos para evaluar riesgos ambientales y planificar estrategias de gestión efectivas, integrando información meteorológica con procesos estocásticos para comprender y prever la dispersión de contaminantes en la atmósfera.

$$$$

## Simulaciones

### Separación de iones usando el potencial ratchet
### Modelo epidemico SIR
### Modelado de dispersión estocástica lagrangiana

## Conclusiones

## Resultados