class Membrane(ThreeDScene):
    def construct(self):
        def u_mn(r, theta, t=0, m=1, n=3):
            b=11.6198
            A=B=C=D=1
            return 0.2*(A*np.cos(b*t) + B*np.sin(b*t))*special.jv(m,b*r)*(C*np.cos(m*theta) + D*np.sin(m*theta))

        def f(dt=0):
            func = lambda r, theta: np.array([r*np.cos(theta),r*np.sin(theta),u_mn(r,theta,dt)])
            obj = Surface(uv_func=func, u_range=(-0.001,1), v_range=(0,TAU), color=BLUE)
            obj.scale(4).rotate(angle=dt*PI/2, axis=OUT).rotate(angle=-PI/3, axis=RIGHT)

            return obj

        current = f()

        def update_membrane(current, alpha):
            dt = interpolate(0,1, alpha)
            new = f(dt)
            current.become(new)

        self.play(FadeIn(current))

        self.play(UpdateFromAlphaFunc(current, update_membrane), rate_func=linear, run_time=5)
        self.wait()
