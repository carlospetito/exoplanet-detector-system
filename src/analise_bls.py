import lightkurve as lk
from astropy.timeseries import BoxLeastSquares
import numpy as np

def load_lightcurve_kic(kic_id):
    lc = lk.search_lightcurve(f"KIC {kic_id}", mission="Kepler").download()
    lc = lc.remove_nans().normalize()
    return lc.time.value, lc.flux.value

def run_bls_on_star(kic_id, tce_row):
    time, flux = load_lightcurve_kic(kic_id)

    bls = BoxLeastSquares(time, flux)
    period_grid = np.linspace(
        tce_row["tce_period"] * 0.5,
        tce_row["tce_period"] * 1.5,
        5000
    )

    results = bls.power(period_grid, tce_row["tce_duration"])

    best_idx = np.argmax(results.power)

    return {
        "period_grid": period_grid,
        "power": results.power,
        "best_period": results.period[best_idx],
        "best_tce_period": tce_row["tce_period"],
    }
