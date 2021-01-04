class Signal:
    def __init__(self, shape, n, amp=1, tk=0, T=1., freq=100):
        """
        Start a signal
        :param shape: format of the signal (step, pulse, sen, random, super_test) string
        :param n: size of the final vector
        :param amp: max amplitude
        :param tk: moment K where some signals "change" (like step or pulse)
        :param T: Period (for timeline construction only)
        :param freq: Frequency of sin signal
        """
        self.len = n
        self.amp = amp
        self.tk = tk
        self.timeline = [round(i*T, 2) for i in range(n)]
        if shape is "step":
            self.values = zeros(n)
            self.values[tk:] = amp
        elif shape is "pulse":
            self.values = zeros(n)
            self.values[tk:tk + 1] = amp
        elif shape is "sen":
            self.values = sin(arr(self.timeline)*freq) * amp + amp
        elif shape is "random":
            self.values = arr([])
            for i in range(100):
                val = random.random() * amp
                self.values = append(self.values, arr([val for _ in range(n//100)]))
        elif shape is "super_test":
            self.values = zeros(n)
            self.values[tk:(tk+n)//2] = amp
            self.values[(tk+n)//2:] = 2 * amp