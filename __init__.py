#!/usr/bin/python3

deposit_with_cpi = lambda x, p, m, t = 0.25: x * (1 + m) * (1 + p * (1- t))

deposit_no_cpi = lambda x, p, t = -0.15: x * (1 + p * (1 - t))
