# Modeling-in-Nature-Science

## Prologo

## Introduction

## Fundamento teorico

### Procesos de Markov

### Ecuaciòn de Langevin, Focker-Planck

### Motor Browniano

$$m\dot{x} = -\frac{dV}{dx} +\frac{1}{m\gamma}F + \sqrt{2D}\xi(t)$$
$$V:\text{Potential ratchet}$$

    
$$V(x)=V_0 \left[C+ \sin \left(2 \pi (x-x_0)  \right) +\frac{1}{4} \sin \left(4 \pi (x-x_0) \right) \right]$$


$$C\approx -1.1 \quad x_0 \approx -1.9$$

### Modelos epidemicos

Modelo SIR clasico

$$S+I+R=N$$

$$\begin{align}
\frac{dS}{dt}&=-\frac{\beta}{N}SI\\
\frac{dI}{dt}&=\frac{\beta}{N}SI-\gamma I\\
\frac{dR}{dt}&=\gamma I
\end{align}$$

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

### Procesos geologicos


## Simulaciones

### Separación de iones
### Modelo SIR
### Erupción volcanica

## Conclusiones

## Resultados