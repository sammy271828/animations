'''
A short animation depicting a family of meromorphic functions having a simple pole which is moving in a circle about two zeros. The code here is modified from that of
the double pendulum simulation video which you can find here:

https://youtu.be/n7JK4Ht8k8M
https://github.com/maksimovichsam/DoublePendulumVideo

'''

class MovingPole(Scene):
    def construct(self):
      
        def f(t=1):
           
            func = lambda z: (4*z-1)**3 * (4*z - 1j) * (4*z + 2*(np.sin(TAU*t) + np.cos(TAU*t)*1j))**(-1)

            def get_between(start, end, proportion):
                return start + (end - start) * proportion

            def radius(z):
                return abs(z)

            def arg(z):
                return np.angle(z)

            def get_color(z):

                z = complex(z.real,z.imag)

                r = np.log(1+abs(z))**0.5
                theta = np.angle(z)

                l = r / (r + 1)
                h = theta
                s = 1

                ratio = h / (math.pi / 3)

                C = (1 - np.abs(2 * l - 1)) * s
                X = C * (1 - np.abs(ratio % 2 - 1))

                m = l - C / 2

                M = np.array([m, m, m])

                ratio = ratio % 6

                if ratio < 1:
                    colors = [C, X, 0]
                elif ratio < 2:
                    colors = [X, C, 0]
                elif ratio < 3:
                    colors = [0, C, X]
                elif ratio < 4:
                    colors = [0, X, C]
                elif ratio < 5:
                    colors = [X, 0, C]
                else:
                    colors = [C, 0, X]

                colors = np.asarray(colors)

                colors = 255 * (colors + M)

                return colors

            def get_coloring(grid_size1,grid_size2):
                n = 1

                data = [[get_color(
                    func(complex(get_between(-n-1/17, n, i / (grid_size1 - 1)), get_between(n,-n, j / (grid_size2 - 1))))) for i in range(grid_size1)] for j in range(grid_size2)]
                return ImageMobject(np.uint8(data))

            grid_size1 = 945
            grid_size2 = 945
            img = get_coloring(grid_size1,grid_size2)

            return img


        def update(c, alpha):
            dt = interpolate(0,1, alpha)
            c_c = f(dt)
            c.become(c_c)

        img = f()
        self.add(img)

        self.play(UpdateFromAlphaFunc(img, update), rate_func=linear, run_time=4)
