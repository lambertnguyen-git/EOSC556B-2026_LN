import numpy as np

def plot_tikhonov_curves(beta_values, phid, phim, n_data=None, beta_index=0, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 3, figsize=(12, 4))

    ax[0].semilogx(beta_values, phid)
    ax[1].semilogx(beta_values, phim)
    ax[2].loglog(phim, phid)

    # highlight chosen beta
    ax[0].semilogx(beta_values[beta_index], phid[beta_index], "ro")
    ax[1].semilogx(beta_values[beta_index], phim[beta_index], "ro")
    ax[2].loglog(phim[beta_index], phid[beta_index], "ro")

    ax[0].set_ylabel(r"$\phi_d$")
    ax[1].set_ylabel(r"$\phi_m$")

    ax[2].set_xlabel(r"$\phi_m$")
    ax[2].set_ylabel(r"$\phi_d$")

    # optional target misfit line
    if n_data is not None:
        ax[0].semilogx(beta_values, np.ones(len(beta_values)) * n_data, "--k")
        ax[2].loglog(phim, np.ones(len(phim)) * n_data, "--k")

    for a in ax[:2]:
        a.invert_xaxis()
        a.set_xlabel(r"$\beta$")

    plt.tight_layout()

    def plot_inversion_results(period, dobs, dpreds, vs_true, mrecs, beta_values, beta_index=0, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # Panel 1: observed vs predicted dispersion
    ax[0].plot(period, dobs, "o", label="observed data")
    ax[0].plot(period, dpreds[:, beta_index], "-s", label="predicted data")
    ax[0].set_xlabel("Period (s)")
    ax[0].set_ylabel("Phase velocity (km/s)")
    ax[0].set_title(f"Dispersion Curve (beta = {beta_values[beta_index]:.2e})")
    ax[0].legend()
    ax[0].grid(True)

    # Panel 2: true model vs recovered model
    layer_index = np.arange(len(vs_true))
    ax[1].plot(vs_true, layer_index, "o-", label="true model")
    ax[1].plot(mrecs[:, beta_index], layer_index, "s--", label="recovered model")
    ax[1].invert_yaxis()
    ax[1].set_xlabel("Vs (km/s)")
    ax[1].set_ylabel("Layer index")
    ax[1].set_title("True vs Recovered Vs Model")
    ax[1].legend()
    ax[1].grid(True)

    plt.tight_layout()