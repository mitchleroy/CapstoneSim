def Atotal(d, r, phi):

    area = ((180-(2 * np.arccos(d/r)))/(360)) * np.pi * r**2 + (d * sqrt(r**2 - d**2)) - (2*phi)
    return area

    