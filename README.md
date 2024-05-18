# Room-Temperature-Simulation
Modelling and controlling temperature flow inside a room with  a PI controller and solving PDE's to make the heat realistic. Added airflow and outside temperature as well as creating a stable environment with feedforward control. Also added a Brownian motion to add in if you are interested.

## Intro
Continuum mechanics is a well-understood subject, but in the construction industry, it is not that simple. One of the great problems of our century is how to solve the Navier-Stokes equations (see this source if interested <a href=https://en.wikipedia.org/wiki/Navier–Stokes_equations>[here]</a>), and this problem has led to countless numerically optimised programs that do just that. These programs account for turbulence, the intricate boundary conditions of the model structure, and optimise for various initial conditions, including weather and outside temperature. However, in most cases, you don't need all of that complexity. Frankly speaking, a simple model goes a long way. That is why I implemented this simple room temperature simulation that regulates a room around 30 degrees Celsius. It is simple, not very realistic, but does the job and intuitively shows the flow of temperature inside a room.

## Glimpse of the Model
Below is a picture from the simulation

## Controller Parameter Settings
When tuning controller parameters in your control systems class, you should always perform your calculations and be very careful. But for a simulation like this, there aren't any dramatic downsides to just testing and tuning manually. We only want reasonable results, not optimized ones, and most importantly, we just want to display a solution. What I am trying to say is that these parameters should work fine:

Also, here is a formula for the PI controller as well as the feedforward control if you are interested. 

$\text{PI Controller Output: } u(t) = K_p \cdot e(t) + K_i \cdot \int e(t) \, dt$


Where:
u(t) is the controller output.
e(t) is the error (the difference between the desired setpoint and the measured process variable).
Kp is the proportional gain.
Ki is the integral gain.

$\text{Feedforward Control Output: } u_{ff} = K_f \cdot d$

Where:
u_ff is the feedforward control output.
Kf is the feedforward gain.
d is the disturbance or the measured variable affecting the process.

If you want to implement this in real life... please do the calculations.
## 
