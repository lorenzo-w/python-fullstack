"""Utils for calculating backpressure of tubing using classical fluid dynamics."""

from fluids.core import K_from_f, Reynolds, dP_from_K
from fluids.fittings import entrance_sharp, exit_normal
from fluids.friction import friction_factor
from pint import UnitRegistry

ureg = UnitRegistry()


def tube_backpressure(
    flow_rate: float,
    diameter: float,
    length: float,
    mu: float,
    rho: float,
) -> float:
    """Calculate the backpressure in a tube due to fluid flow.

    Args:
      flow_rate: Volumetric flow rate in mL/min
      diameter: in mm
      length: in mm
      mu: in kg/m^3
      rho: in Pa.s
    Returns:
      backpressure in Pa
    """
    # Note: Using pint for unit conversions where convenient.
    v_m_s = (
        ((flow_rate * ureg.mL / ureg.min) / (3.14159 * (diameter * ureg.mm / 2) ** 2))
        .to("m/s")  # pyright: ignore[reportAttributeAccessIssue]
        .magnitude
    )
    d_m = (
        (diameter * ureg.mm)
        .to("m")  # pyright: ignore[reportAttributeAccessIssue]
        .magnitude
    )
    l_m = (
        (length * ureg.mm)
        .to("m")  # pyright: ignore[reportAttributeAccessIssue]
        .magnitude
    )

    reynolds = Reynolds(
        V=v_m_s,  # pyright: ignore[reportArgumentType]
        D=d_m,  # pyright: ignore[reportArgumentType]
        rho=rho,
        mu=mu,
    )
    fd = friction_factor(
        Re=reynolds,
        eD=1e-4,  # assume some roughness
    )

    k = K_from_f(
        fd=fd,
        L=l_m,  # pyright: ignore[reportArgumentType]
        D=d_m,  # pyright: ignore[reportArgumentType]
    )
    k += entrance_sharp() * 5
    k += exit_normal() * 5

    return dP_from_K(
        K=k,
        rho=rho,
        V=v_m_s,  # pyright: ignore[reportArgumentType]
    )
