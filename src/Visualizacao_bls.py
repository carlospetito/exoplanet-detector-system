import matplotlib.pyplot as plt

def plot_bls_comparison(bls_result):
    plt.figure(figsize=(10,4))
    plt.plot(bls_result["period_grid"], bls_result["power"])
    plt.axvline(bls_result["best_tce_period"], color="red", linestyle="--", label="TCE")
    plt.axvline(bls_result["best_period"], color="green", linestyle="--", label="BLS")
    plt.legend()
    plt.title("Comparação: TCE vs Período Detectado via BLS")
    plt.xlabel("Período (dias)")
    plt.ylabel("BLS Power")
    plt.show()
