from opensemantic.characteristics.quantitative._static import QuantityValue, UnitEnum
from typing import Any, Optional
from pydantic.v1 import Field

class MobilityUnit(UnitEnum):
    meter_squared_per_second_per_volt = "Item:OSWb2b78d963e4e54d7b5e64db90eb5fad2"
    centi_meter_squared_per_second_per_volt = (
        "Item:OSWb2b78d963e4e54d7b5e64db90eb5fad2#OSW5912aba53a8b5951ae88d643b40ff33d"
    )


class Mobility(QuantityValue):
    """
    "Mobility" characterizes how quickly a particle can move through a metal or semiconductor, when pulled by an electric field. The average drift speed imparted to a charged particle in a medium by an electric field, divided by the electric field strength.
    """

    type: Optional[Any] = ["Category:OSWb11e150b382c5481b59c763f0d4794fb"]
    unit: Optional[MobilityUnit] = Field(
        MobilityUnit.meter_squared_per_second_per_volt, title="MobilityUnit"
    )

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


class MolarFluxDensityUnit(UnitEnum):
    mole_per_meter_squared_per_second = "Item:OSW3063bab947d256b1a7a11cdb158d11b1"
    milli_mole_per_meter_squared_per_second = (
        "Item:OSW3063bab947d256b1a7a11cdb158d11b1#OSWd5bf9cdb27765d8bbc553cf3682b1c52"
    )
    micro_mole_per_meter_squared_per_second = (
        "Item:OSW3063bab947d256b1a7a11cdb158d11b1#OSW92a55c5f59b259f8acfe7284e9f7ebe1"
    )


class MolarFluxDensity(QuantityValue):
    """
    the rate at which moles of a substance pass through a unit area per unit time. It is used for describing the flow of materials in terms of the transport of molecules or particles rather than bulk mass. The SI units are mol m-2 s-1
    """

    type: Optional[Any] = ["Category:OSW00dbaeb24c2952cd9ad29928be2f1b83"]
    unit: Optional[MolarFluxDensityUnit] = Field(
        MolarFluxDensityUnit.mole_per_meter_squared_per_second,
        title="MolarFluxDensityUnit",
    )

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


class ElectricCurrentPerTemperatureUnit(UnitEnum):
    ampere_per_Celsius = "Item:OSW167de6aa22ae5b798f9914c5468307c3"


class ElectricCurrentPerTemperature(QuantityValue):
    """
    "Electric Current per Temperature" is used to express how a current is subject to temperature. Originally used in Wien's Law to describe phenomena related to filaments. One use today is to express how a current generator derates with temperature.
    """

    type: Optional[Any] = ["Category:OSW442f95e934355966b4f87f1d5ed06b13"]
    unit: Optional[ElectricCurrentPerTemperatureUnit] = Field(
        ElectricCurrentPerTemperatureUnit.ampere_per_Celsius,
        title="ElectricCurrentPerTemperatureUnit",
    )

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


class InductanceUnit(UnitEnum):
    henry = "Item:OSWfc7ffe7e6e00592a8b3f3f472fbef2a2"
    pico_henry = (
        "Item:OSWfc7ffe7e6e00592a8b3f3f472fbef2a2#OSWc916910c94335ef4bfd4956fdb64d445"
    )
    micro_henry = (
        "Item:OSWfc7ffe7e6e00592a8b3f3f472fbef2a2#OSW0b6f22fdf4505cd1a14ced6ce63fd1c3"
    )
    milli_henry = (
        "Item:OSWfc7ffe7e6e00592a8b3f3f472fbef2a2#OSWf936212f93685b0a81e881b7b4cd691c"
    )
    nano_henry = (
        "Item:OSWfc7ffe7e6e00592a8b3f3f472fbef2a2#OSW466788b3b91054088792f8efcf881b73"
    )


class Inductance(QuantityValue):
    """
    "Inductance" is an electromagentic quantity that characterizes a circuit's resistance to any change of electric current; a change in the electric current through induces an opposing electromotive force (EMF). Quantitatively, inductance is proportional to the magnetic flux per unit of electric current.
    """

    type: Optional[Any] = ["Category:OSW704290344ec45e1bb91d2b2736233473"]
    unit: Optional[InductanceUnit] = Field(InductanceUnit.henry, title="InductanceUnit")

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


class VaporPermeabilityUnit(UnitEnum):
    kilo_gram_per_meter_per_pascal_per_second = (
        "Item:OSWa2b4ab78b9975e0891d0d14dfbb12314"
    )


class VaporPermeability(QuantityValue):
    """
    The moisture transmission rate of a material is referred to as its "permeability".
    """

    type: Optional[Any] = ["Category:OSW8a68e1f32c6a525fb76f292b5bee6b5b"]
    unit: Optional[VaporPermeabilityUnit] = Field(
        VaporPermeabilityUnit.kilo_gram_per_meter_per_pascal_per_second,
        title="VaporPermeabilityUnit",
    )

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


class DiffusionCoefficientUnit(UnitEnum):
    meter_squared_per_second = "Item:OSW20b837bfd2fa5c3abc86347ce702f27c"
    milli_meter_squared_per_second = (
        "Item:OSW20b837bfd2fa5c3abc86347ce702f27c#OSW5db8f161eb8c59129cef62d84dd3309c"
    )
    centi_meter_squared_per_second = (
        "Item:OSW20b837bfd2fa5c3abc86347ce702f27c#OSW031bb99ee99a5794a24c66e6203c21db"
    )


class DiffusionCoefficient(QuantityValue):
    """
    The "Diffusion Coefficient" is
    """

    type: Optional[Any] = ["Category:OSW1bfa314830e85a74ba42f89688132372"]
    unit: Optional[DiffusionCoefficientUnit] = Field(
        DiffusionCoefficientUnit.meter_squared_per_second,
        title="DiffusionCoefficientUnit",
    )

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


class SurfaceCoefficientOfHeatTransferUnit(UnitEnum):
    watt_per_kelvin_per_meter_squared = "Item:OSWdc31cad7e9225defbc08f6f79bf5c4ea"


class SurfaceCoefficientOfHeatTransfer(QuantityValue):
    """
    This is an autogenerated partial class definition of 'SurfaceCoefficientOfHeatTransfer'
    """

    type: Optional[Any] = ["Category:OSW7423002c2fd45809bfc0c4879b7d6f9c"]
    unit: Optional[SurfaceCoefficientOfHeatTransferUnit] = Field(
        SurfaceCoefficientOfHeatTransferUnit.watt_per_kelvin_per_meter_squared,
        title="SurfaceCoefficientOfHeatTransferUnit",
    )
