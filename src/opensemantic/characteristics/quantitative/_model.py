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



class ExposureRateUnit(UnitEnum):
    coulomb_per_kilo_gram_per_second = "Item:OSW7c9817a1145157e8b2803464c641e6cf"


class ExposureRate(QuantityValue):
    """
    "Exposure Rate" expresses the rate of charge production per unit mass of air and is commonly expressed in roentgens per hour (R/h) or milliroentgens per hour (mR/h).
    """

    type: Optional[Any] = ["Category:OSW759cf8e16f60598887292ea131ad71c2"]
    unit: Optional[ExposureRateUnit] = Field(
        ExposureRateUnit.coulomb_per_kilo_gram_per_second, title="ExposureRateUnit"
    )



class ConductivityUnit(UnitEnum):
    siemens_per_meter = "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d"
    pico_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWc9f2986f0974565b904f1d0d756d5318"
    )
    milli_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWd609b57361b3560d8614f22a0031921f"
    )
    nano_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW6cc3591d052d589cb271f6710f816486"
    )
    mega_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW27b6c423e529517ba2d3f466d2c822b4"
    )
    micro_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWa26d6194b3be5f54a4665a01e3df9426"
    )
    siemens_per_centi_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW88703a966490546d89632c3336e28b2a"
    )
    kilo_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWe2d30b3b09325ef7819f6d51071e147e"
    )
    deci_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW7b2e1f125aa350409a4f5d467534727a"
    )


class Conductivity(QuantityValue):
    """
    "Conductivity" is a scalar or tensor quantity the product of which by the electric field strength in a medium is equal to the electric current density. For an isotropic medium the conductivity is a scalar quantity; for an anisotropic medium it is a tensor quantity.
    """

    type: Optional[Any] = ["Category:OSW44eec22e65f759d99d9efa4c5dc5b54f"]
    unit: Optional[ConductivityUnit] = Field(
        ConductivityUnit.siemens_per_meter, title="ConductivityUnit"
    )



class RichardsonConstantUnit(UnitEnum):
    ampere_per_kelvin_squared_per_meter_squared = (
        "Item:OSW958d74176efb543f819fe576e03621fa"
    )


class RichardsonConstant(QuantityValue):
    """
    "Richardson Constant" is a constant used in developing thermionic emission current density for a metal.
    """

    type: Optional[Any] = ["Category:OSWa78b60b5e433540bba1f2970c4a21f07"]
    unit: Optional[RichardsonConstantUnit] = Field(
        RichardsonConstantUnit.ampere_per_kelvin_squared_per_meter_squared,
        title="RichardsonConstantUnit",
    )



class MassPerLengthUnit(UnitEnum):
    kilo_gram_per_meter = (
        "Item:OSW0429f89d17e6572fac6630caa443c336#OSW1e1793e6b72454f1a81b08eabc8272b7"
    )


class MassPerLength(QuantityValue):
    """
    Linear density, linear mass density or linear mass is a measure of mass per unit of length, and it is a characteristic of strings or other one-dimensional objects. The SI unit of linear density is the kilogram per metre ($kg/m$).
    """

    type: Optional[Any] = ["Category:OSWc1785119277b56f0b8b069c41b019d06"]
    unit: Optional[MassPerLengthUnit] = Field(
        MassPerLengthUnit.kilo_gram_per_meter, title="MassPerLengthUnit"
    )



class RotationalMassUnit(UnitEnum):
    kilo_gram_meter_squared = "Item:OSWd211fc61709b5e48a4c96473c86a8d13"


class RotationalMass(QuantityValue):
    """
    "Rotational Mass" denotes the inertia of a body with respect to angular acceleration. It is usually measured in kg*m^2.
    """

    type: Optional[Any] = ["Category:OSWe1ce3c9278dd5766b37e01a7c94e5445"]
    unit: Optional[RotationalMassUnit] = Field(
        RotationalMassUnit.kilo_gram_meter_squared, title="RotationalMassUnit"
    )



class BasicityUnit(UnitEnum):
    pico_henry = "Item:OSW50e9172c55045cb3b1460b1345303ed2"


class Basicity(QuantityValue):
    """
    Chemicals or substances having a pH higher than 7 are said to be basic; higher pH means higher basicity.
    """

    type: Optional[Any] = ["Category:OSW8189a49e2c98599a8c635dbbfaa6b5b6"]
    unit: Optional[BasicityUnit] = Field(BasicityUnit.pico_henry, title="BasicityUnit")



class SpecificAcousticImpedanceUnit(UnitEnum):
    newton_second_per_meter_cubed = "Item:OSW4ba64f5b6daa583389742dfca1776afe"


class SpecificAcousticImpedance(QuantityValue):
    """
    This is an autogenerated partial class definition of 'SpecificAcousticImpedance'
    """

    type: Optional[Any] = ["Category:OSWc00b3d7abb405127b2b492f5bda88d14"]
    unit: Optional[SpecificAcousticImpedanceUnit] = Field(
        SpecificAcousticImpedanceUnit.newton_second_per_meter_cubed,
        title="SpecificAcousticImpedanceUnit",
    )



class EnergyUnit(UnitEnum):
    joule = "Item:OSW730568cd7ae65906abbbcef1d15cb074"
    peta_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW4e7003f5d7ff58a190167711dd63b0bd"
    )
    kilo_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWad2518d42b685f569679c3599455c3d3"
    )
    milli_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW6df751011258508e9d15967190c819f3"
    )
    femto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW2d5cdc08b064506e8f9a5b0456b7a0b3"
    )
    tera_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW0ac3643d930d5c99936e5ece487a9634"
    )
    exa_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW5ba80670b2945c08b35551442d3169d5"
    )
    giga_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc26bf1cf449d56ef8122745336585d2b"
    )
    mega_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc1525b1f1fc05c40b9715328bf707805"
    )
    atto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWa73c696efa58519aa07c265ea965ceda"
    )


class Energy(QuantityValue):
    """
    Energy is the quantity characterizing the ability of a system to do work.
    """

    type: Optional[Any] = ["Category:OSWc87ddd4a7d1159f0a75b686a61ef4e8e"]
    unit: Optional[EnergyUnit] = Field(EnergyUnit.joule, title="EnergyUnit")



class ElectricFluxUnit(UnitEnum):
    meter_volt = "Item:OSW45282d4f758259de9032e1df3d80d870"


class ElectricFlux(QuantityValue):
    """
    "Electric Flux" through an area is defined as the electric field multiplied by the area of the surface projected in a plane perpendicular to the field. Electric Flux is a scalar-valued quantity.
    """

    type: Optional[Any] = ["Category:OSWcddea398bde45403a70adb55b09c0053"]
    unit: Optional[ElectricFluxUnit] = Field(
        ElectricFluxUnit.meter_volt, title="ElectricFluxUnit"
    )



class ResidualResistivityUnit(UnitEnum):
    meter_ohm = "Item:OSW825f941d934e5a73866e39b6c42c99f0"


class ResidualResistivity(QuantityValue):
    """
    "Residual Resistivity" for metals, is the resistivity extrapolated to zero thermodynamic temperature.
    """

    type: Optional[Any] = ["Category:OSW773f040f505b58938f7ee54e1b7eb29f"]
    unit: Optional[ResidualResistivityUnit] = Field(
        ResidualResistivityUnit.meter_ohm, title="ResidualResistivityUnit"
    )



class LinearEnergyTransferUnit(UnitEnum):
    joule_per_meter = "Item:OSW0505357de255592eb766bdfce883acb3"


class LinearEnergyTransfer(QuantityValue):
    """
    "Linear Energy Transfer"  (LET) is the linear density of energy lost by a charged ionizing particle travelling through matter.Typically, this measure is used to quantify the effects of ionizing radiation on biological specimens or electronic devices.
    """

    type: Optional[Any] = ["Category:OSWe471db8fa7d85359a1ad86773c4d671b"]
    unit: Optional[LinearEnergyTransferUnit] = Field(
        LinearEnergyTransferUnit.joule_per_meter, title="LinearEnergyTransferUnit"
    )



class SectionAreaIntegralUnit(UnitEnum):
    field_5 = "Item:OSWe03debd3c6025a95b236f88c61ba0bac"


class SectionAreaIntegral(QuantityValue):
    """
    The sectional area integral measure is typically used in torsional analysis. It is usually measured in M⁵.
    """

    type: Optional[Any] = ["Category:OSWe6d85f03e75c5740a25a00bc1ebb03a8"]
    unit: Optional[SectionAreaIntegralUnit] = Field(
        SectionAreaIntegralUnit.field_5, title="SectionAreaIntegralUnit"
    )



class NEONUnit(UnitEnum):
    Celsius_squared = "Item:OSWd9cb8583836d53228ac7907d5bf8f0f9"


class NEON(QuantityValue):
    """
    Variance for NEON temperature data measured in degrees celcius
    """

    type: Optional[Any] = ["Category:OSWcb65eb7ce36c5a1a8b3b0684f4476fca"]
    unit: Optional[NEONUnit] = Field(NEONUnit.Celsius_squared, title="NEONUnit")



class BloodGlucoseLevelUnit(UnitEnum):
    milli_mole_per_liter = (
        "Item:OSW58a109c7b24256769e6f6716407aff58#OSW42ad2b521cac599c9a5f08e3edd7d88a"
    )


class BloodGlucoseLevel(QuantityValue):
    """
    Blood sugar level, blood sugar concentration, or blood glucose level is the amount of glucose present in the blood of humans and animals.
      Glucose is a simple sugar and approximately 4 grams of glucose are present in the blood of humans at all times.
      Stored in skeletal muscle and liver cells in the form of glycogen, the body tightly regulates blood glucose levels as a part of metabolic homeostasis.
      During fasting blood glucose is maintained at a constant level at the expense of the glycogen stores in the liver and skeletal muscle.
      There are two main methods of describing concentrations: by weight, and by molecular count.
      Weights are in grams and molecular counts in moles.
      A mole is $6.022\times 10^{23}$ molecules.
      In both cases, the unit is usually modified by $milli-$ or $micro-$ or other prefix,
       and is always $per$ some volume, often a litre.
      Conversion factors depend on the molecular weight of the substance in question.
      $mmol/L$ is millimoles/liter, and is the world standard unit for measuring glucose in blood.
      Specifically, it is the designated SI (Systeme International) unit.
      Some countries use $mg/dl$.
      A mole is about $6\times 10^{23}$ molecules.
      $mg/dL$ (milligrams/deciliter) is the traditional unit for measuring $bG$ (blood glucose).
      There is a trend toward using $mmol/L$ however $mg/dL$ is much in practice.
      Some use is made of $mmol/L$ as the primary unit with $mg/dL$ quoted in parentheses.
      This acknowledges the large base of health care providers, researchers and patients who are already familiar with $mg/dL$.
    """

    type: Optional[Any] = ["Category:OSW0f23b91fa3605c65a1e002e9a2fa0f10"]
    unit: Optional[BloodGlucoseLevelUnit] = Field(
        BloodGlucoseLevelUnit.milli_mole_per_liter, title="BloodGlucoseLevelUnit"
    )



class ElectricChargeLinearDensityUnit(UnitEnum):
    coulomb_per_meter = "Item:OSW375890764ffa5a5cb84e1cbbe16a7315"


class ElectricChargeLinearDensity(QuantityValue):
    """
    In electromagnetism, charge density is a measure of electric charge per unit volume of space, in one, two or three dimensions. More specifically: the linear, surface, or volume charge density is the amount of electric charge per unit length, surface area, or volume, respectively.
    """

    type: Optional[Any] = ["Category:OSW4631a0c82e5a5333b3a89b76ff2d0b54"]
    unit: Optional[ElectricChargeLinearDensityUnit] = Field(
        ElectricChargeLinearDensityUnit.coulomb_per_meter,
        title="ElectricChargeLinearDensityUnit",
    )



class ElectricPolarizabilityUnit(UnitEnum):
    joule_per_mole = "Item:OSW7e66beeef6b05637a554d3506d689000"
    kilo_joule_per_mole = (
        "Item:OSW7e66beeef6b05637a554d3506d689000#OSW23b10a54326955adb1862933713551f9"
    )


class ElectricPolarizability(QuantityValue):
    """
    "Electric Polarizability" is the relative tendency of a charge distribution, like the electron cloud of an atom or molecule, to be distorted from its normal shape by an external electric field, which is applied typically by inserting the molecule in a charged parallel-plate capacitor, but may also be caused by the presence of a nearby ion or dipole.
    """

    type: Optional[Any] = ["Category:OSWad99acb7711152a5ad91363577e00430"]
    unit: Optional[ElectricPolarizabilityUnit] = Field(
        ElectricPolarizabilityUnit.joule_per_mole, title="ElectricPolarizabilityUnit"
    )



class NonActivePowerUnit(UnitEnum):
    volt_ampere = "Item:OSWb41c4bc68f7951658a66c7481061c1f2"
    mega_volt_ampere = (
        "Item:OSWb41c4bc68f7951658a66c7481061c1f2#OSWecfc0485465d510aa98f09bb3aafabef"
    )
    kilo_volt_ampere = (
        "Item:OSWb41c4bc68f7951658a66c7481061c1f2#OSWcafa0565b412503b86477319f5bb3187"
    )


class NonActivePower(QuantityValue):
    """
    "Non-active Power", for a two-terminal element or a two-terminal circuit under periodic conditions, is the quantity equal to the square root of the difference of the squares of the apparent power and the active power.
    """

    type: Optional[Any] = ["Category:OSW43581783e8e657828615687e07a1d3e8"]
    unit: Optional[NonActivePowerUnit] = Field(
        NonActivePowerUnit.volt_ampere, title="NonActivePowerUnit"
    )



class SlowingDownDensityUnit(UnitEnum):
    per_meter_cubed_per_second = "Item:OSW804e40f82f4955ab8f1bd0c1e9e77d28"


class SlowingDownDensity(QuantityValue):
    """
    "Slowing-Down Density" is a measure of the rate at which neutrons lose energy in a nuclear reactor through collisions; equal to the number of neutrons that fall below a given energy per unit volume per unit time.
    """

    type: Optional[Any] = ["Category:OSW72e926f2d87e540c84ff1fa039adef5e"]
    unit: Optional[SlowingDownDensityUnit] = Field(
        SlowingDownDensityUnit.per_meter_cubed_per_second,
        title="SlowingDownDensityUnit",
    )



class ParticleFluenceRateUnit(UnitEnum):
    per_meter_squared_per_second = "Item:OSW580b455ce69e57418303f409d43f373a"


class ParticleFluenceRate(QuantityValue):
    """
    "Particle Fluence Rate" can be defined as the total number of particles (typically Gamma Ray Photons ) crossing over a sphere of unit cross section which surrounds a Point Source of Ionising Radiation.
    """

    type: Optional[Any] = ["Category:OSW674cc9976cb75a02ad5c78a671459acd"]
    unit: Optional[ParticleFluenceRateUnit] = Field(
        ParticleFluenceRateUnit.per_meter_squared_per_second,
        title="ParticleFluenceRateUnit",
    )



class PhaseCoefficientUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class PhaseCoefficient(QuantityValue):
    """
    The phase coefficient is the amount of phase shift that occurs as the wave travels one meter. Increasing the loss of the material, via the manipulation of the material's conductivity, will decrease the wavelength (increase $\beta$) and increase the attenuation coefficient (increase $\alpha$).
    """

    type: Optional[Any] = ["Category:OSW023d5e3256055be3a9350a1c4f1a3ba3"]
    unit: Optional[PhaseCoefficientUnit] = Field(
        PhaseCoefficientUnit.per_meter, title="PhaseCoefficientUnit"
    )



class NuclearQuadrupoleMomentUnit(UnitEnum):
    meter_squared = "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9"
    centi_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWe36916dd7a34557b8a52c38d6dd7b832"
    )
    milli_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWeca22bf4270853038ef3395bd6dd797b"
    )
    micro_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWd45e991f8e6658dcb6c891c9c0ea094f"
    )
    nano_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSW8ef862bedf335232a9d387b1ee29cd1d"
    )
    deci_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSW90aaf1cb6a9f518a8e7ed0b7fc2fc325"
    )


class NuclearQuadrupoleMoment(QuantityValue):
    """
    "Nuclear Quadrupole Moment" is a quantity that characterizes the deviation from spherical symmetry of the electrical charge distribution in an atomic nucleus.
    """

    type: Optional[Any] = ["Category:OSW7e9c76bc94c25dc8929bc8fe039ecf8f"]
    unit: Optional[NuclearQuadrupoleMomentUnit] = Field(
        NuclearQuadrupoleMomentUnit.meter_squared, title="NuclearQuadrupoleMomentUnit"
    )



class SecondPolarMomentOfAreaUnit(UnitEnum):
    field_4 = "Item:OSWe4f01fe00389574e905718a14481ed36"
    field_4_1 = (
        "Item:OSWe4f01fe00389574e905718a14481ed36#OSW73b630d93619585bbc7f4a3a4a3be104"
    )
    field_4_2 = (
        "Item:OSWe4f01fe00389574e905718a14481ed36#OSW568d0d17db6551c1993de3d51c6051cc"
    )


class SecondPolarMomentOfArea(QuantityValue):
    """
    The moment of inertia, also called mass moment of inertia, rotational inertia, polar moment of inertia of mass, or the angular mass is a property of a distribution of mass in space that measures its resistance to rotational acceleration about an axis.
    """

    type: Optional[Any] = ["Category:OSW8bbfb552acb854199f8cef7cf24ce319"]
    unit: Optional[SecondPolarMomentOfAreaUnit] = Field(
        SecondPolarMomentOfAreaUnit.field_4, title="SecondPolarMomentOfAreaUnit"
    )



class SpecificImpulseByWeightUnit(UnitEnum):
    second = "Item:OSW85302b21cf045998b80f38c9fdb88f84"
    deci_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW78488a0c8e885365beff30aae10a4efd"
    )
    micro_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW90ff22cff2dd5d8ba6de84bf9a70c50c"
    )
    atto_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW2e4fec0373f45f1891403f06e433c5eb"
    )
    pico_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWc6f2918cbdef5bde8d00cf86938c7f8e"
    )
    milli_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW84d4f530814e5251b06e73ee0184e32b"
    )
    femto_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWd1e24421c83d5defb5c22e9a5fe490fb"
    )
    nano_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW14e2efd7a4a05306a74663592edb23e8"
    )
    kilo_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWbc38445f00d056069fef04f8e25c66f6"
    )


class SpecificImpulseByWeight(QuantityValue):
    """
    This is an autogenerated partial class definition of 'SpecificImpulseByWeight'
    """

    type: Optional[Any] = ["Category:OSW48d809902b445a6ca8ecae9e3fdfbcf0"]
    unit: Optional[SpecificImpulseByWeightUnit] = Field(
        SpecificImpulseByWeightUnit.second, title="SpecificImpulseByWeightUnit"
    )



class EnergyPerElectricChargeUnit(UnitEnum):
    volt = "Item:OSW85efe1428cb75363a75aab6435e2d98d"
    milli_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW82d25d00b1485cc18c204f95de4536a9"
    )
    micro_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSWc0cb09a94aa553589a59ea70bfccfc96"
    )
    kilo_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW4deed980237a5360b48e0dd1331d4199"
    )
    mega_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW78798aa1bdcb57f0aea8d4eb86ff3355"
    )


class EnergyPerElectricCharge(QuantityValue):
    """
    Voltage is a representation of the electric potential energy per unit charge. If a unit of electrical charge were placed in a location, the voltage indicates the potential energy of it at that point. In other words, it is a measurement of the energy contained within an electric field, or an electric circuit, at a given point. Voltage is a scalar quantity. The SI unit of voltage is the volt, such that $1 volt = 1 joule/coulomb$.
    """

    type: Optional[Any] = ["Category:OSWce9a8c0dfd2159b2a628364ae9fbe9f3"]
    unit: Optional[EnergyPerElectricChargeUnit] = Field(
        EnergyPerElectricChargeUnit.volt, title="EnergyPerElectricChargeUnit"
    )



class MagneticFluxPerLengthUnit(UnitEnum):
    newton_per_ampere = "Item:OSWefcd851d718352018f7355bf1594398e"


class MagneticFluxPerLength(QuantityValue):
    """
    "Magnetic Flux per Length" is a quantity in the SI and C.G.S. Systems of Quantities.
    """

    type: Optional[Any] = ["Category:OSWbb4c4273347b5d59b4d0b083dd8135a5"]
    unit: Optional[MagneticFluxPerLengthUnit] = Field(
        MagneticFluxPerLengthUnit.newton_per_ampere, title="MagneticFluxPerLengthUnit"
    )



class EnergyPerTemperatureUnit(UnitEnum):
    joule_per_kelvin = "Item:OSW501738b1f645568c9c4fb6da844439c7"
    kilo_joule_per_kelvin = (
        "Item:OSW501738b1f645568c9c4fb6da844439c7#OSW7b31ddba89fc5359972c09eda7f30683"
    )
    mega_joule_per_kelvin = (
        "Item:OSW501738b1f645568c9c4fb6da844439c7#OSWf8925d2e60865f589809095c9e172dbe"
    )


class EnergyPerTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'EnergyPerTemperature'
    """

    type: Optional[Any] = ["Category:OSWc16b766eaf3e547da6407e8eee408e7c"]
    unit: Optional[EnergyPerTemperatureUnit] = Field(
        EnergyPerTemperatureUnit.joule_per_kelvin, title="EnergyPerTemperatureUnit"
    )



class MassPerTimeUnit(UnitEnum):
    newton_second_per_meter = "Item:OSW69c99f1ab4825dffbf3578e6d04cd58e"


class MassPerTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'MassPerTime'
    """

    type: Optional[Any] = ["Category:OSWb61a75d702365027b17cfa7e8ae10cb3"]
    unit: Optional[MassPerTimeUnit] = Field(
        MassPerTimeUnit.newton_second_per_meter, title="MassPerTimeUnit"
    )



class TimeUnit(UnitEnum):
    second = "Item:OSW85302b21cf045998b80f38c9fdb88f84"
    deci_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW78488a0c8e885365beff30aae10a4efd"
    )
    micro_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW90ff22cff2dd5d8ba6de84bf9a70c50c"
    )
    atto_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW2e4fec0373f45f1891403f06e433c5eb"
    )
    pico_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWc6f2918cbdef5bde8d00cf86938c7f8e"
    )
    milli_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW84d4f530814e5251b06e73ee0184e32b"
    )
    femto_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWd1e24421c83d5defb5c22e9a5fe490fb"
    )
    nano_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW14e2efd7a4a05306a74663592edb23e8"
    )
    kilo_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWbc38445f00d056069fef04f8e25c66f6"
    )


class Time(QuantityValue):
    """
    Time is a basic component of the measuring system used to sequence events, to compare the durations of events and the intervals between them, and to quantify the motions of objects.
    """

    type: Optional[Any] = ["Category:OSW389cb87d31be515aa5d2f12e2b66e938"]
    unit: Optional[TimeUnit] = Field(TimeUnit.second, title="TimeUnit")



class ThomsonCoefficientUnit(UnitEnum):
    volt_per_kelvin = "Item:OSW8998763d58065a069429e7e6fe3c153a"


class ThomsonCoefficient(QuantityValue):
    """
    "Thomson Coefficient" represents Thomson heat power developed, divided by the electric current and the temperature difference.
    """

    type: Optional[Any] = ["Category:OSWc56f5d63f59d527e9a105d4c7edda71e"]
    unit: Optional[ThomsonCoefficientUnit] = Field(
        ThomsonCoefficientUnit.volt_per_kelvin, title="ThomsonCoefficientUnit"
    )



class SpectralRadiantEnergyDensityUnit(UnitEnum):
    field_4 = "Item:OSW9660b61081145dbcb6d4ebb5ab9244ff"


class SpectralRadiantEnergyDensity(QuantityValue):
    """
    "Spectral Radiant Energy Density" is the spectral concentration of radiant energy density (in terms of wavelength), or the spectral radiant energy density (in terms of wave length).
    """

    type: Optional[Any] = ["Category:OSW8ec996b0f248559db27d621ab9651953"]
    unit: Optional[SpectralRadiantEnergyDensityUnit] = Field(
        SpectralRadiantEnergyDensityUnit.field_4,
        title="SpectralRadiantEnergyDensityUnit",
    )



class AngularReciprocalLatticeVectorUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class AngularReciprocalLatticeVector(QuantityValue):
    """
    "Angular Reciprocal Lattice Vector" is a vector whose scalar products with all fundamental lattice vectors are integral multiples of $2\pi$.
    """

    type: Optional[Any] = ["Category:OSW0dca3665339d53b2aeb2c152dc1ff577"]
    unit: Optional[AngularReciprocalLatticeVectorUnit] = Field(
        AngularReciprocalLatticeVectorUnit.per_meter,
        title="AngularReciprocalLatticeVectorUnit",
    )



class ForcePerLengthUnit(UnitEnum):
    newton_per_meter = "Item:OSW0d4e5e11d53f5018a0b965373b55510d"


class ForcePerLength(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ForcePerLength'
    """

    type: Optional[Any] = ["Category:OSW4496d2b66d71545392a81e9e05297338"]
    unit: Optional[ForcePerLengthUnit] = Field(
        ForcePerLengthUnit.newton_per_meter, title="ForcePerLengthUnit"
    )



class LorenzCoefficientUnit(UnitEnum):
    volt_squared_per_kelvin_squared = "Item:OSW2ef02698f9245a488ed2d3f996ca14a0"


class LorenzCoefficient(QuantityValue):
    """
    "Lorenz Coefficient" is part mof the Lorenz curve.
    """

    type: Optional[Any] = ["Category:OSW3861c9ccb54a566789b4b9c93410b6e6"]
    unit: Optional[LorenzCoefficientUnit] = Field(
        LorenzCoefficientUnit.volt_squared_per_kelvin_squared,
        title="LorenzCoefficientUnit",
    )



class VolumicElectromagneticEnergyUnit(UnitEnum):
    joule_per_meter_cubed = "Item:OSW9ea4bf89c42b56728392f1c55639ac18"
    mega_joule_per_meter_cubed = (
        "Item:OSW9ea4bf89c42b56728392f1c55639ac18#OSW7044da5ba4b45554b3acc6c6f3fc3624"
    )


class VolumicElectromagneticEnergy(QuantityValue):
    """
    $\textit{Volumic Electromagnetic Energy}$, also known as the $\textit{Electromagnetic Energy Density}$, is the energy associated with an electromagnetic field, per unit volume of the field.
    """

    type: Optional[Any] = ["Category:OSWcfe6332cb5935e5cb59602e245a610cd"]
    unit: Optional[VolumicElectromagneticEnergyUnit] = Field(
        VolumicElectromagneticEnergyUnit.joule_per_meter_cubed,
        title="VolumicElectromagneticEnergyUnit",
    )



class InverseTimeTemperatureUnit(UnitEnum):
    hertz_per_kelvin = "Item:OSW21febbc735d25a9badefe5f3191757d9"
    mega_hertz_per_kelvin = (
        "Item:OSW21febbc735d25a9badefe5f3191757d9#OSW1214143f4aa952e78f3ec1c339d9500b"
    )


class InverseTimeTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseTimeTemperature'
    """

    type: Optional[Any] = ["Category:OSW95d7cb8ca1db560eb936826b8f4444bc"]
    unit: Optional[InverseTimeTemperatureUnit] = Field(
        InverseTimeTemperatureUnit.hertz_per_kelvin, title="InverseTimeTemperatureUnit"
    )



class TemperatureUnit(UnitEnum):
    kelvin = "Item:OSWe728730c00ea5cf9af66a550e51b9717"


class Temperature(QuantityValue):
    """
    Temperature is a physical property of matter that quantitatively expresses the common notions of hot and cold. Objects of low temperature are cold, while various degrees of higher temperatures are referred to as warm or hot. Heat spontaneously flows from bodies of a higher temperature to bodies of lower temperature, at a rate that increases with the temperature difference and the thermal conductivity.
    """

    type: Optional[Any] = ["Category:OSW20927e4900e95e93985698c92995f964"]
    unit: Optional[TemperatureUnit] = Field(
        TemperatureUnit.kelvin, title="TemperatureUnit"
    )



class PermeanceUnit(UnitEnum):
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


class Permeance(QuantityValue):
    """
    "Permeance" is the inverse of reluctance. Permeance is a measure of the quantity of flux for a number of current-turns in magnetic circuit. A magnetic circuit almost acts as though the flux is "conducted", therefore permeance is larger for large cross sections of a material and smaller for longer lengths. This concept is analogous to electrical conductance in the electric circuit.
    """

    type: Optional[Any] = ["Category:OSW80e9cf7556915b54b8326b588abc2531"]
    unit: Optional[PermeanceUnit] = Field(PermeanceUnit.henry, title="PermeanceUnit")



class DensityUnit(UnitEnum):
    gram_per_liter = "Item:OSW754b1a3564725113ac583f91ae2ea959"
    milli_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWca4043a385f25aa3a98122f2aefd0d2e"
    )
    micro_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW457d0485a44c57cda788a583bf9ab4ff"
    )
    gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWe905ceb23b3b550489bed5baa6c9b466"
    )
    kilo_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW40c933269ec45fc1aeef04aefce2b374"
    )
    pico_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW84ec459d4d135bf28a610cd00061d18c"
    )
    milli_gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW99bbcff947e1508bad38d748ad6ff8e2"
    )
    gram_per_deci_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW1a48aea5dca45c34bbde02b0df02f6f8"
    )
    femto_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW449dc7494f3f5c0bbd9aff1d1fd2f591"
    )
    nano_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW42fdef27c8ae5c8fbf1876c400f27101"
    )


class Density(QuantityValue):
    """
    The mass density or density of a material is defined as its mass per unit volume.
      The symbol most often used for density is $\rho$.
       Mathematically, density is defined as mass divided by volume: $\rho = m/V$,
        where $\rho$ is the density, $m$ is the mass, and $V$ is the volume.
        In some cases, density is also defined as its weight per unit volume, although this quantity is more properly called specific weight.
    """

    type: Optional[Any] = ["Category:OSW571f68d4b4715284b2dc5020ad51cf72"]
    unit: Optional[DensityUnit] = Field(DensityUnit.gram_per_liter, title="DensityUnit")



class TemperaturePerTimeSquaredUnit(UnitEnum):
    kelvin_per_second_squared = "Item:OSW44905d403bba5525b7b95b2325c87b42"


class TemperaturePerTimeSquared(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TemperaturePerTimeSquared'
    """

    type: Optional[Any] = ["Category:OSW3023cedc530751a18804888ed56cdca5"]
    unit: Optional[TemperaturePerTimeSquaredUnit] = Field(
        TemperaturePerTimeSquaredUnit.kelvin_per_second_squared,
        title="TemperaturePerTimeSquaredUnit",
    )



class ForcePerAngleUnit(UnitEnum):
    newton_per_radian = "Item:OSW1a0a52ba2fe957989fe3e1a2d0bbdcc4"


class ForcePerAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ForcePerAngle'
    """

    type: Optional[Any] = ["Category:OSW15c4097ed256572c97e7a1dbbfb154dd"]
    unit: Optional[ForcePerAngleUnit] = Field(
        ForcePerAngleUnit.newton_per_radian, title="ForcePerAngleUnit"
    )



class SpecificVolumeUnit(UnitEnum):
    meter_cubed_per_kilo_gram = "Item:OSW8967238ff12d589a8e1383b0a684ddc5"
    milli_meter_cubed_per_kilo_gram = (
        "Item:OSW8967238ff12d589a8e1383b0a684ddc5#OSW0e4d5b9c7d1557418a789c8360d239cb"
    )


class SpecificVolume(QuantityValue):
    """
    "Specific Volume" ($\nu$) is the volume occupied by a unit of mass of a material. It is equal to the inverse of density.
    """

    type: Optional[Any] = ["Category:OSW26ae18e11ed158dc9ea7e62d1d5ce92e"]
    unit: Optional[SpecificVolumeUnit] = Field(
        SpecificVolumeUnit.meter_cubed_per_kilo_gram, title="SpecificVolumeUnit"
    )



class InverseSquareEnergyUnit(UnitEnum):
    per_joule_squared = "Item:OSW0dddefef8d455a10adeaafa69cd3afd7"


class InverseSquareEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseSquareEnergy'
    """

    type: Optional[Any] = ["Category:OSWd14639032128589bbb33cfd08b009878"]
    unit: Optional[InverseSquareEnergyUnit] = Field(
        InverseSquareEnergyUnit.per_joule_squared, title="InverseSquareEnergyUnit"
    )



class TimeSquaredUnit(UnitEnum):
    second_squared = "Item:OSW00ec6531e2fb5ba8aee8cf8852860aed"


class TimeSquared(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TimeSquared'
    """

    type: Optional[Any] = ["Category:OSWc676d11273eb5903ac59330fbbdfee18"]
    unit: Optional[TimeSquaredUnit] = Field(
        TimeSquaredUnit.second_squared, title="TimeSquaredUnit"
    )



class EnergyPerSquareMagneticFluxDensityUnit(UnitEnum):
    joule_per_tesla_squared = "Item:OSW462714679d475b158c530d359d42de44"


class EnergyPerSquareMagneticFluxDensity(QuantityValue):
    """
    "Energy Per Square Magnetic Flux Density" is a measure of energy for a unit of magnetic flux density.
    """

    type: Optional[Any] = ["Category:OSWe5b6e1c95287515f8cf9255397d5848b"]
    unit: Optional[EnergyPerSquareMagneticFluxDensityUnit] = Field(
        EnergyPerSquareMagneticFluxDensityUnit.joule_per_tesla_squared,
        title="EnergyPerSquareMagneticFluxDensityUnit",
    )



class MagneticTensionUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class MagneticTension(QuantityValue):
    """
    Magnetic Tension is a scalar quantity equal to the line integral of the magnetic field strength H along a specified path linking two points a and b.
    """

    type: Optional[Any] = ["Category:OSWb08c515569015c02ba889380cb0808ff"]
    unit: Optional[MagneticTensionUnit] = Field(
        MagneticTensionUnit.ampere, title="MagneticTensionUnit"
    )



class MassicActivityUnit(UnitEnum):
    becquerel_per_kilo_gram = "Item:OSW03b25e9a7cef5adeb7f3d5f82115dfc3"
    milli_becquerel_per_kilo_gram = (
        "Item:OSW03b25e9a7cef5adeb7f3d5f82115dfc3#OSWc896c96c6de8521181daee0118de2c5b"
    )
    micro_becquerel_per_kilo_gram = (
        "Item:OSW03b25e9a7cef5adeb7f3d5f82115dfc3#OSW23b3668ed7d3501da40aaa0a4e9f765e"
    )


class MassicActivity(QuantityValue):
    """
    "Massic Activity" is the activity divided by the total mass of the sample.
    """

    type: Optional[Any] = ["Category:OSW9cb88f0c339451c59ecf9587128ee4b5"]
    unit: Optional[MassicActivityUnit] = Field(
        MassicActivityUnit.becquerel_per_kilo_gram, title="MassicActivityUnit"
    )



class SpecificOpticalRotatoryPowerUnit(UnitEnum):
    meter_squared_radian_per_kilo_gram = "Item:OSW555ce8e01951566b8507f419b1987b04"


class SpecificOpticalRotatoryPower(QuantityValue):
    """
    The "Specific Optical Rotatory Power" Angle of optical rotation divided by the optical path length through the medium and by the mass concentration of the substance giving the specific optical rotatory power.
    """

    type: Optional[Any] = ["Category:OSW77e8f77ce04f54e9a4f3d616427252b6"]
    unit: Optional[SpecificOpticalRotatoryPowerUnit] = Field(
        SpecificOpticalRotatoryPowerUnit.meter_squared_radian_per_kilo_gram,
        title="SpecificOpticalRotatoryPowerUnit",
    )



class SurfaceDensityUnit(UnitEnum):
    kilo_gram_per_meter_squared = (
        "Item:OSWb93e608c86fd5480a5de9cd1b3e9ea22#OSW86b6ab5f70aa5624be17645333d53d51"
    )


class SurfaceDensity(QuantityValue):
    """
    The area density (also known as areal density, surface density, or superficial density) of a two-dimensional object is calculated as the mass per unit area.
    """

    type: Optional[Any] = ["Category:OSWa1191d6116125618b9cb06db9d0b49be"]
    unit: Optional[SurfaceDensityUnit] = Field(
        SurfaceDensityUnit.kilo_gram_per_meter_squared, title="SurfaceDensityUnit"
    )



class VolumeUnit(UnitEnum):
    meter_cubed = "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8"
    milli_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSWa9d92cf2bcb95b1887a23f99b51d8d36"
    )
    deca_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSW5024fe1a02365460bbc23fa2e8a46a7b"
    )
    micro_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSW7126d9f54e0b565898ccf21988c04366"
    )
    centi_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSWcd2df951f11a56d2a06705a8f16b0662"
    )
    deci_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSWdda7ee9dea455958af1466a861d5bf7d"
    )


class Volume(QuantityValue):
    """
    The volume of a solid object is the three-dimensional concept of how much space it occupies, often quantified numerically. One-dimensional figures (such as lines) and two-dimensional shapes (such as squares) are assigned zero volume in the three-dimensional space.
    """

    type: Optional[Any] = ["Category:OSWf5c54cd70ddf5ff3b1ef1aee6ae8f0cb"]
    unit: Optional[VolumeUnit] = Field(VolumeUnit.meter_cubed, title="VolumeUnit")



class VolumePerUnitAreaUnit(UnitEnum):
    meter = "Item:OSWa2c814499650570090ea4ac058c81e3b"


class VolumePerUnitArea(QuantityValue):
    """
    This is an autogenerated partial class definition of 'VolumePerUnitArea'
    """

    type: Optional[Any] = ["Category:OSWc64d0369be9152ea97312548eb67383d"]
    unit: Optional[VolumePerUnitAreaUnit] = Field(
        VolumePerUnitAreaUnit.meter, title="VolumePerUnitAreaUnit"
    )



class PhotonIntensityUnit(UnitEnum):
    per_second_per_steradian = "Item:OSWaf6c62c0856f5ac288ac862f5344f227"


class PhotonIntensity(QuantityValue):
    """
    A measure of flux of photons per solid angle
    """

    type: Optional[Any] = ["Category:OSW24bf224c3e2a57b6a896f3cd3b9395b2"]
    unit: Optional[PhotonIntensityUnit] = Field(
        PhotonIntensityUnit.per_second_per_steradian, title="PhotonIntensityUnit"
    )



class EnergyDensityOfStatesUnit(UnitEnum):
    per_joule_per_meter_cubed = "Item:OSW397d9707b473555a8b294558cbc5d2a1"


class EnergyDensityOfStates(QuantityValue):
    """
    "Energy Density of States" refers to electrons or other entities, e.g. phonons. It can, for example, refer to amount of substance instead of volume.
    """

    type: Optional[Any] = ["Category:OSWcd73bd1d42a75671896bbf11ed611b6e"]
    unit: Optional[EnergyDensityOfStatesUnit] = Field(
        EnergyDensityOfStatesUnit.per_joule_per_meter_cubed,
        title="EnergyDensityOfStatesUnit",
    )



class KermaRateUnit(UnitEnum):
    gray_per_second = "Item:OSW4cbc32faa6945fea85c32ee675aff008"


class KermaRate(QuantityValue):
    """
    "Kerma Rate" is the kerma per unit time.
    """

    type: Optional[Any] = ["Category:OSWe08b19a7b5ef582882979b450b729fe6"]
    unit: Optional[KermaRateUnit] = Field(
        KermaRateUnit.gray_per_second, title="KermaRateUnit"
    )



class LinearCompressibilityUnit(UnitEnum):
    micro_meter_per_newton = "Item:OSWdf7665f78da1599c98a13586cec6d866"


class LinearCompressibility(QuantityValue):
    """
    Linear Compressibility is a measure of the relative length change of a solid as a response to a normal force change.
    """

    type: Optional[Any] = ["Category:OSWd15c0a83636b5e1293aaef6b1e619c4f"]
    unit: Optional[LinearCompressibilityUnit] = Field(
        LinearCompressibilityUnit.micro_meter_per_newton,
        title="LinearCompressibilityUnit",
    )



class AttenuationCoefficientUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class AttenuationCoefficient(QuantityValue):
    """
    The attenuation coefficient is a quantity that characterizes how easily a material or medium can be penetrated by a beam of light, sound, particles, or other energy or matter. A large attenuation coefficient means that the beam is quickly "attenuated" (weakened) as it passes through the medium, and a small attenuation coefficient means that the medium is relatively transparent to the beam. The Attenuation Coefficient is also called linear attenuation coefficient, narrow beam attenuation coefficient, or absorption coefficient.
    """

    type: Optional[Any] = ["Category:OSW0ead3c6cf6115beeb175b122432d24a7"]
    unit: Optional[AttenuationCoefficientUnit] = Field(
        AttenuationCoefficientUnit.per_meter, title="AttenuationCoefficientUnit"
    )



class LinearVelocityUnit(UnitEnum):
    meter_per_second = "Item:OSW78331234e1a15aeebd8b0caa71201939"
    centi_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWd094e4cfd62c52248aad5ef87c19fb7d"
    )
    micro_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWfc9fca27ba5b543c8780521b4af39189"
    )
    milli_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW4937ac85021f506cb7ba3958f2216bd1"
    )
    kilo_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW9f12ce12bc725cd59791265e2e480fd2"
    )


class LinearVelocity(QuantityValue):
    """
    Linear Velocity, as the name implies deals with speed in a straight line, the units are often $km/hr$ or $m/s$ or $mph$ (miles per hour). Linear Velocity (v) = change in distance/change in time, where $v = \bigtriangleup d/\bigtriangleup t$
    """

    type: Optional[Any] = ["Category:OSWa05bb9d48dca5745bee355865a3109f2"]
    unit: Optional[LinearVelocityUnit] = Field(
        LinearVelocityUnit.meter_per_second, title="LinearVelocityUnit"
    )



class MomentumUnit(UnitEnum):
    newton_second = "Item:OSWb05df920a96b5987aeb46a9b4f7ca333"


class Momentum(QuantityValue):
    """
    The momentum of a system of particles is given by the sum of the momentums of the individual particles which make up the system or by the product of the total mass of the system and the velocity of the center of gravity of the system. The momentum of a continuous medium is given by the integral of the velocity over the mass of the medium or by the product of the total mass of the medium and the velocity of the center of gravity of the medium.
    """

    type: Optional[Any] = ["Category:OSWfcd8d6e69a0d595bb4e9fb4969abf37c"]
    unit: Optional[MomentumUnit] = Field(
        MomentumUnit.newton_second, title="MomentumUnit"
    )



class TemperaturePerTimeUnit(UnitEnum):
    Celsius_per_second = "Item:OSW90e277e1e16052a49c728adea4b95d64"


class TemperaturePerTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TemperaturePerTime'
    """

    type: Optional[Any] = ["Category:OSWb124402a1c76538b81dd41babc0cd7e2"]
    unit: Optional[TemperaturePerTimeUnit] = Field(
        TemperaturePerTimeUnit.Celsius_per_second, title="TemperaturePerTimeUnit"
    )



class ModulusOfElasticityUnit(UnitEnum):
    pascal = "Item:OSWb663e6bff3595e7b93b28fffce66c50c"
    giga_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW49bb4743a5735e189777f3c6bd422a52"
    )
    deca_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW8d40059d9e3951bb97378fe3f119ba21"
    )
    milli_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW38b0e12539b05ce28cd126c8eea29f95"
    )
    mega_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW0ec5bf8132b25e58b7032766bd9b3225"
    )
    kilo_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW264ebdc21f54568593a91bbd832b6fbf"
    )
    hecto_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW482939f123595314beca39ad32d65a15"
    )
    micro_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW5def4be309ce50ee933c99cf4b74e310"
    )


class ModulusOfElasticity(QuantityValue):
    """
    The Modulus of Elasticity is the mathematical description of an object or substance's tendency to be deformed elastically (that is, non-permanently) when a force is applied to it.
    """

    type: Optional[Any] = ["Category:OSWb341ca5380495b7e992e1d7cf3c06ddc"]
    unit: Optional[ModulusOfElasticityUnit] = Field(
        ModulusOfElasticityUnit.pascal, title="ModulusOfElasticityUnit"
    )



class HydraulicPermeabilityUnit(UnitEnum):
    meter_squared = "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9"
    centi_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWe36916dd7a34557b8a52c38d6dd7b832"
    )
    milli_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWeca22bf4270853038ef3395bd6dd797b"
    )
    micro_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWd45e991f8e6658dcb6c891c9c0ea094f"
    )
    nano_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSW8ef862bedf335232a9d387b1ee29cd1d"
    )
    deci_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSW90aaf1cb6a9f518a8e7ed0b7fc2fc325"
    )


class HydraulicPermeability(QuantityValue):
    """
    Permeability is a property of porous materials that is an indication of the ability for fluids (gas or liquid) to flow through them. Fluids can more easily flow through a material with high permeability than one with low permeability. The permeability of a medium is related to the porosity, but also to the shapes of the pores in the medium and their level of connectedness.
    """

    type: Optional[Any] = ["Category:OSW1999834eda4e5e4f89dc83c98c0bb609"]
    unit: Optional[HydraulicPermeabilityUnit] = Field(
        HydraulicPermeabilityUnit.meter_squared, title="HydraulicPermeabilityUnit"
    )



class ElectricPotentialUnit(UnitEnum):
    volt = "Item:OSW85efe1428cb75363a75aab6435e2d98d"
    milli_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW82d25d00b1485cc18c204f95de4536a9"
    )
    micro_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSWc0cb09a94aa553589a59ea70bfccfc96"
    )
    kilo_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW4deed980237a5360b48e0dd1331d4199"
    )
    mega_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW78798aa1bdcb57f0aea8d4eb86ff3355"
    )


class ElectricPotential(QuantityValue):
    """
    The Electric Potential is a scalar valued quantity associated with an electric field. The electric potential $\phi(x)$ at a point, $x$, is formally defined as the line integral of the electric field taken along a path from x to the point at infinity. If the electric field is static, that is time independent, then the choice of the path is arbitrary; however if the electric field is time dependent, taking the integral a different paths will produce different results.
    """

    type: Optional[Any] = ["Category:OSWe88cb4482e6e587d922c9004a3d73a8d"]
    unit: Optional[ElectricPotentialUnit] = Field(
        ElectricPotentialUnit.volt, title="ElectricPotentialUnit"
    )



class ReciprocalMassUnit(UnitEnum):
    per_gram = "Item:OSW779e33a057275cba9d6f363a1526d8bf"


class ReciprocalMass(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ReciprocalMass'
    """

    type: Optional[Any] = ["Category:OSW01d40c436663572d80de0e503436a120"]
    unit: Optional[ReciprocalMassUnit] = Field(
        ReciprocalMassUnit.per_gram, title="ReciprocalMassUnit"
    )



class MassPerAreaTimeUnit(UnitEnum):
    gram_per_day_per_meter_squared = "Item:OSWb2902ae1df0b561682bfc174af5ff039"
    milli_gram_per_day_per_meter_squared = (
        "Item:OSWb2902ae1df0b561682bfc174af5ff039#OSW93a70588ce305c56aa1c3d6417632649"
    )
    micro_gram_per_day_per_meter_squared = (
        "Item:OSWb2902ae1df0b561682bfc174af5ff039#OSWae40efaa247650f38362d522eabf49ca"
    )


class MassPerAreaTime(QuantityValue):
    """
    In Physics and Engineering, mass flux is the rate of mass flow per unit area. The common symbols are $j$, $J$, $\phi$, or $\Phi$  (Greek lower or capital Phi), sometimes with subscript $m$ to indicate mass is the flowing quantity.  Its SI units are $ kg s^{-1} m^{-2}$.
    """

    type: Optional[Any] = ["Category:OSW9e775ee5d35455faaa88953b35b2d911"]
    unit: Optional[MassPerAreaTimeUnit] = Field(
        MassPerAreaTimeUnit.gram_per_day_per_meter_squared, title="MassPerAreaTimeUnit"
    )



class ModulusOfSubgradeReactionUnit(UnitEnum):
    newton_per_meter_cubed = "Item:OSWf3f9733d84285a338b5b7306145c9b6d"
    kilo_newton_per_meter_cubed = (
        "Item:OSWf3f9733d84285a338b5b7306145c9b6d#OSWfe42a11de5995fa380fbde579c89484c"
    )


class ModulusOfSubgradeReaction(QuantityValue):
    """
    Modulus of Subgrade Reaction is a geotechnical measure describing interaction between foundation structures and the soil. May also be known as bedding measure. Usually measured in N/m3.
    """

    type: Optional[Any] = ["Category:OSWa74a41713cc154b88da68cd2d1399e71"]
    unit: Optional[ModulusOfSubgradeReactionUnit] = Field(
        ModulusOfSubgradeReactionUnit.newton_per_meter_cubed,
        title="ModulusOfSubgradeReactionUnit",
    )



class ForcePerAreaTimeUnit(UnitEnum):
    pascal_per_second = "Item:OSWda81752da4a7532fb7d5790cd2e41a1c"


class ForcePerAreaTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ForcePerAreaTime'
    """

    type: Optional[Any] = ["Category:OSW5ffdbf4db0e95c7e8ce0298e48ee3197"]
    unit: Optional[ForcePerAreaTimeUnit] = Field(
        ForcePerAreaTimeUnit.pascal_per_second, title="ForcePerAreaTimeUnit"
    )



class IsothermalCompressibilityUnit(UnitEnum):
    per_pascal = "Item:OSWf030abd4441d52a7a8c5f84950985ea4"


class IsothermalCompressibility(QuantityValue):
    """
    The isothermal compressibility defines the rate of change of system volume with pressure.
    """

    type: Optional[Any] = ["Category:OSW3c3443b8e1395c6f986793f1d9f7d27a"]
    unit: Optional[IsothermalCompressibilityUnit] = Field(
        IsothermalCompressibilityUnit.per_pascal, title="IsothermalCompressibilityUnit"
    )



class TemperatureAmountOfSubstanceUnit(UnitEnum):
    Celsius_mole = "Item:OSW0e7c411abb9050609e99957558d70536"


class TemperatureAmountOfSubstance(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TemperatureAmountOfSubstance'
    """

    type: Optional[Any] = ["Category:OSW7d5feb9968315612a4cceccd238be582"]
    unit: Optional[TemperatureAmountOfSubstanceUnit] = Field(
        TemperatureAmountOfSubstanceUnit.Celsius_mole,
        title="TemperatureAmountOfSubstanceUnit",
    )



class ElectricChargeDensityUnit(UnitEnum):
    coulomb_per_meter_cubed = "Item:OSW138cfd775f5f5791acb676b2e30a858b"
    giga_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSWa2ef417cc76554ccbc1e21d3399b1d0f"
    )
    mega_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW78239b85b3255c27b70c82b5d719f312"
    )
    micro_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW7ff981494feb573893427df6c288c2c1"
    )
    coulomb_per_milli_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW6684ece78b035280a9997fd7e0946a64"
    )
    coulomb_per_centi_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSWf658e9170de757b99c1b492865347a7e"
    )
    kilo_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSWabb39bf77e53590aafd85088c14233eb"
    )
    milli_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW0cf667e041bf5c70ad88948e99591fa7"
    )


class ElectricChargeDensity(QuantityValue):
    """
    In electromagnetism, charge density is a measure of electric charge per unit volume of space, in one, two or three dimensions. More specifically: the linear, surface, or volume charge density is the amount of electric charge per unit length, surface area, or volume, respectively.
    """

    type: Optional[Any] = ["Category:OSWd5b78fad165c5fae8a856a349a1997e1"]
    unit: Optional[ElectricChargeDensityUnit] = Field(
        ElectricChargeDensityUnit.coulomb_per_meter_cubed,
        title="ElectricChargeDensityUnit",
    )



class MeanMassRangeUnit(UnitEnum):
    kilo_gram_per_meter_squared = (
        "Item:OSWb93e608c86fd5480a5de9cd1b3e9ea22#OSW86b6ab5f70aa5624be17645333d53d51"
    )


class MeanMassRange(QuantityValue):
    """
    "Mean Mass Range" is the mean linear range multiplied by the mass density of the material.
    """

    type: Optional[Any] = ["Category:OSWe1380e899bfe51bdab985a0c3581e8c4"]
    unit: Optional[MeanMassRangeUnit] = Field(
        MeanMassRangeUnit.kilo_gram_per_meter_squared, title="MeanMassRangeUnit"
    )



class SpecificModulusUnit(UnitEnum):
    meter_squared_per_second_squared = "Item:OSWf6d6f2af61295484ab10221fe5922f97"
    kilo_meter_squared_per_second_squared = (
        "Item:OSWf6d6f2af61295484ab10221fe5922f97#OSWf19ea831be1053a9b70d6403acc15022"
    )


class SpecificModulus(QuantityValue):
    """
    <p><b>Specific modulus</b> is a <a href="/wiki/Materials_property" class="mw-redirect" title="Materials property">materials property</a> consisting of the <a href="/wiki/Elastic_modulus" title="Elastic modulus">elastic modulus</a> per mass <a href="/wiki/Density" title="Density">density</a> of a material. It is also known as the <b>stiffness to weight ratio</b> or <b>specific stiffness</b>. High specific modulus materials find wide application in <a href="/wiki/Aerospace" title="Aerospace">aerospace</a> applications where minimum structural <a href="/wiki/Weight" title="Weight">weight</a> is required. The <a href="/wiki/Dimensional_analysis" title="Dimensional analysis">dimensional analysis</a> yields units of distance squared per time squared.</p>
    """

    type: Optional[Any] = ["Category:OSW2aeee06f4fdf5b97bc4bb4c3893af100"]
    unit: Optional[SpecificModulusUnit] = Field(
        SpecificModulusUnit.meter_squared_per_second_squared,
        title="SpecificModulusUnit",
    )



class LinearAccelerationUnit(UnitEnum):
    meter_per_second_squared = "Item:OSWb91fd68d93375855a57c795180c429a3"
    centi_meter_per_second_squared = (
        "Item:OSWb91fd68d93375855a57c795180c429a3#OSW014676a1d72e5f16a59a8d966253ab6f"
    )


class LinearAcceleration(QuantityValue):
    """
    This is an autogenerated partial class definition of 'LinearAcceleration'
    """

    type: Optional[Any] = ["Category:OSWa2a2e32d40b65c90b0cd1b4af5e0c6d2"]
    unit: Optional[LinearAccelerationUnit] = Field(
        LinearAccelerationUnit.meter_per_second_squared, title="LinearAccelerationUnit"
    )



class SurfaceActivityDensityUnit(UnitEnum):
    becquerel_per_meter_squared = "Item:OSW8369e204ddec5045893b3249ff474d53"


class SurfaceActivityDensity(QuantityValue):
    """
    The "Surface Activity Density" is undefined.
    """

    type: Optional[Any] = ["Category:OSWc2294c7dee7252b4a277d3e03eb1e8f8"]
    unit: Optional[SurfaceActivityDensityUnit] = Field(
        SurfaceActivityDensityUnit.becquerel_per_meter_squared,
        title="SurfaceActivityDensityUnit",
    )



class LengthTemperatureUnit(UnitEnum):
    kelvin_meter = "Item:OSWe5ae11f7ed995d13bdf12af6c0a8a444"


class LengthTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'LengthTemperature'
    """

    type: Optional[Any] = ["Category:OSWd28e781886de5a3fbab07eefc7bb9aa2"]
    unit: Optional[LengthTemperatureUnit] = Field(
        LengthTemperatureUnit.kelvin_meter, title="LengthTemperatureUnit"
    )



class MolarAbsorptionCoefficientUnit(UnitEnum):
    meter_squared_per_mole = "Item:OSWf4a7837882ed5a0b9b128b2d067fc97b"


class MolarAbsorptionCoefficient(QuantityValue):
    """
    "Molar Absorption Coefficient" is a spectrophotometric unit indicating the light a substance absorbs with respect to length, usually centimeters, and concentration, usually moles per liter.
    """

    type: Optional[Any] = ["Category:OSWf7cbdd37870f51bfb9f262d8bb177df7"]
    unit: Optional[MolarAbsorptionCoefficientUnit] = Field(
        MolarAbsorptionCoefficientUnit.meter_squared_per_mole,
        title="MolarAbsorptionCoefficientUnit",
    )



class AreaUnit(UnitEnum):
    meter_squared = "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9"
    centi_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWe36916dd7a34557b8a52c38d6dd7b832"
    )
    milli_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWeca22bf4270853038ef3395bd6dd797b"
    )
    micro_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSWd45e991f8e6658dcb6c891c9c0ea094f"
    )
    nano_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSW8ef862bedf335232a9d387b1ee29cd1d"
    )
    deci_meter_squared = (
        "Item:OSWd10e5841c68e5aad94b481b58ef9dfb9#OSW90aaf1cb6a9f518a8e7ed0b7fc2fc325"
    )


class Area(QuantityValue):
    """
    Area is a quantity expressing the two-dimensional size of a defined part of a surface, typically a region bounded by a closed curve.
    """

    type: Optional[Any] = ["Category:OSW1fcf1694712e5684885071efdf775bd9"]
    unit: Optional[AreaUnit] = Field(AreaUnit.meter_squared, title="AreaUnit")



class ElectricCurrentPhasorUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class ElectricCurrentPhasor(QuantityValue):
    """
    "Electric Current Phasor" is a representation of current as a sinusoidal integral quantity using a complex quantity whose argument is equal to the initial phase and whose modulus is equal to the root-mean-square value. A phasor is a constant complex number, usually expressed in exponential form, representing the complex amplitude (magnitude and phase) of a sinusoidal function of time. Phasors are used by electrical engineers to simplify computations involving sinusoids, where they can often reduce a differential equation problem to an algebraic one.
    """

    type: Optional[Any] = ["Category:OSW01c55f7ea3ee516a8b469146bd45b3b6"]
    unit: Optional[ElectricCurrentPhasorUnit] = Field(
        ElectricCurrentPhasorUnit.ampere, title="ElectricCurrentPhasorUnit"
    )



class LinearThermalExpansionUnit(UnitEnum):
    meter_per_kelvin = "Item:OSWb2550b7d752e505bb62ecc632d6c20f9"
    micro_meter_per_kelvin = (
        "Item:OSWb2550b7d752e505bb62ecc632d6c20f9#OSW8aabb581b81c50b688909bbc187a92d1"
    )
    centi_meter_per_kelvin = (
        "Item:OSWb2550b7d752e505bb62ecc632d6c20f9#OSW3585b69d1b325a36918e362b36dcd2b9"
    )
    milli_meter_per_kelvin = (
        "Item:OSWb2550b7d752e505bb62ecc632d6c20f9#OSW023c203283725c8b814a69dd13cfcb92"
    )


class LinearThermalExpansion(QuantityValue):
    """
    When the temperature of a substance changes, the energy that is stored in the intermolecular bonds between atoms changes. When the stored energy increases, so does the length of the molecular bonds. As a result, solids typically expand in response to heating and contract on cooling; this dimensional response to temperature change is expressed by its coefficient of thermal expansion. Different coefficients of thermal expansion can be defined for a substance depending on whether the expansion is measured by: linear thermal expansion, area thermal expansion, or volumetric thermal expansion.
    """

    type: Optional[Any] = ["Category:OSWcbd09a3b3c5356f6b501044b7a9cd13b"]
    unit: Optional[LinearThermalExpansionUnit] = Field(
        LinearThermalExpansionUnit.meter_per_kelvin, title="LinearThermalExpansionUnit"
    )



class CatalyticActivityUnit(UnitEnum):
    katal = "Item:OSW73fc60d9e1dd5337a5f4befdc3646012"


class CatalyticActivity(QuantityValue):
    """
    An index of the actual or potential activity of a catalyst. The catalytic activity of an enzyme or an enzyme-containing preparation is defined as the property measured by the increase in the rate of conversion of a specified chemical reaction that the enzyme produces in a specified assay system. Catalytic activity is an extensive quantity and is a property of the enzyme, not of the reaction mixture; it is thus conceptually different from rate of conversion although measured by and equidimensional with it. The unit for catalytic activity is the $katal$; it may also be expressed in mol $s^{-1}$. Dimensions: $N T^{-1}$. Former terms such as catalytic ability, catalytic amount, and enzymic activity are no er recommended. Derived quantities are molar catalytic activity, specific catalytic activity, and catalytic activity concentration. Source(s): <a href="http://www.answers.com/topic/catalytic-activity-biochemistry">www.answers.com</a>
    """

    type: Optional[Any] = ["Category:OSWbe5794638aff5dcdb9fd6a34466c98b4"]
    unit: Optional[CatalyticActivityUnit] = Field(
        CatalyticActivityUnit.katal, title="CatalyticActivityUnit"
    )



class MassPerElectricChargeUnit(UnitEnum):
    second_tesla = "Item:OSW5935489883d15f2fb2ef853f57c66f49"


class MassPerElectricCharge(QuantityValue):
    """
    The mass-to-charge ratio ratio ($m/Q$) is a physical quantity that is widely used in the electrodynamics of charged particles, for example, in electron optics and ion optics. The importance of the mass-to-charge ratio, according to classical electrodynamics, is that two particles with the same mass-to-charge ratio move in the same path in a vacuum when subjected to the same electric and magnetic fields. Its SI units are $kg/C$, but it can also be measured in Thomson ($Th$).
    """

    type: Optional[Any] = ["Category:OSW81c50bcd5413593ab0b892c5612090fe"]
    unit: Optional[MassPerElectricChargeUnit] = Field(
        MassPerElectricChargeUnit.second_tesla, title="MassPerElectricChargeUnit"
    )



class TotalMassStoppingPowerUnit(UnitEnum):
    joule_meter_squared_per_kilo_gram = "Item:OSWe0fa484f50015a438e4338bb521a34ae"


class TotalMassStoppingPower(QuantityValue):
    """
    If a substance is compared in gaseous and solid form, then the linear stopping powers of the two states are very different just because of the different density. One therefore often divides S(E) by the density of the material to obtain the "Mass Stopping Power". The mass stopping power then depends only very little on the density of the material.
    """

    type: Optional[Any] = ["Category:OSWc02cab0088b05f12b174944247c8e903"]
    unit: Optional[TotalMassStoppingPowerUnit] = Field(
        TotalMassStoppingPowerUnit.joule_meter_squared_per_kilo_gram,
        title="TotalMassStoppingPowerUnit",
    )



class ElectricChargeVolumeDensityUnit(UnitEnum):
    coulomb_per_meter_cubed = "Item:OSW138cfd775f5f5791acb676b2e30a858b"
    giga_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSWa2ef417cc76554ccbc1e21d3399b1d0f"
    )
    mega_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW78239b85b3255c27b70c82b5d719f312"
    )
    micro_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW7ff981494feb573893427df6c288c2c1"
    )
    coulomb_per_milli_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW6684ece78b035280a9997fd7e0946a64"
    )
    coulomb_per_centi_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSWf658e9170de757b99c1b492865347a7e"
    )
    kilo_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSWabb39bf77e53590aafd85088c14233eb"
    )
    milli_coulomb_per_meter_cubed = (
        "Item:OSW138cfd775f5f5791acb676b2e30a858b#OSW0cf667e041bf5c70ad88948e99591fa7"
    )


class ElectricChargeVolumeDensity(QuantityValue):
    """
    In electromagnetism, charge density is a measure of electric charge per unit volume of space, in one, two or three dimensions. More specifically: the linear, surface, or volume charge density is the amount of electric charge per unit length, surface area, or volume, respectively. The respective SI units are $C \cdot m^{-1}$, $C \cdot m^{-2}$ or $C \cdot m^{-3}$.
    """

    type: Optional[Any] = ["Category:OSWef9be82e83295e35a630f2703fd7595d"]
    unit: Optional[ElectricChargeVolumeDensityUnit] = Field(
        ElectricChargeVolumeDensityUnit.coulomb_per_meter_cubed,
        title="ElectricChargeVolumeDensityUnit",
    )



class TimeTemperatureUnit(UnitEnum):
    kelvin_second = "Item:OSW258e0e8da8e15fd69ec6810d5b93c7ab"


class TimeTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TimeTemperature'
    """

    type: Optional[Any] = ["Category:OSW6f81fb79192f50e280ee1ff5dd724f01"]
    unit: Optional[TimeTemperatureUnit] = Field(
        TimeTemperatureUnit.kelvin_second, title="TimeTemperatureUnit"
    )



class PolarisabilityUnit(UnitEnum):
    coulomb_squared_meter_squared_per_joule = "Item:OSW9ed3650077ea5a42931687ccd72f11ba"


class Polarisability(QuantityValue):
    """
    Maß für die Deformierbarkeit der Elektronenhülle von Molekülen und Atomen
    """

    type: Optional[Any] = ["Category:OSW428688cfd14256ef999765241fd57f9e"]
    unit: Optional[PolarisabilityUnit] = Field(
        PolarisabilityUnit.coulomb_squared_meter_squared_per_joule,
        title="PolarisabilityUnit",
    )



class SpectralCrossSectionUnit(UnitEnum):
    meter_squared_per_joule = "Item:OSW06fd6479544b5a6db5427ff73da63ee9"


class SpectralCrossSection(QuantityValue):
    """
    "Spectral Cross-section" is the cross-section for a process in which the energy of the ejected or scattered particle is in an interval of energy, divided by the range $dE$ of this interval.
    """

    type: Optional[Any] = ["Category:OSWeec705c7a60052698e01058732a6d8de"]
    unit: Optional[SpectralCrossSectionUnit] = Field(
        SpectralCrossSectionUnit.meter_squared_per_joule,
        title="SpectralCrossSectionUnit",
    )



class InverseSquareMassUnit(UnitEnum):
    per_kilo_gram_squared = "Item:OSWea9499724b3152d5a6090f9ef5ce7f4a"


class InverseSquareMass(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseSquareMass'
    """

    type: Optional[Any] = ["Category:OSW345e44042c495fcda2a9c0e0d67739be"]
    unit: Optional[InverseSquareMassUnit] = Field(
        InverseSquareMassUnit.per_kilo_gram_squared, title="InverseSquareMassUnit"
    )



class CombinedNonEvaporativeHeatTransferCoefficientUnit(UnitEnum):
    watt_per_kelvin_per_meter_squared = "Item:OSWdc31cad7e9225defbc08f6f79bf5c4ea"


class CombinedNonEvaporativeHeatTransferCoefficient(QuantityValue):
    """
    "Combined Non Evaporative Heat Transfer Coefficient" is the
    """

    type: Optional[Any] = ["Category:OSWa4e5b51256a65c60be793f4224e41487"]
    unit: Optional[CombinedNonEvaporativeHeatTransferCoefficientUnit] = Field(
        CombinedNonEvaporativeHeatTransferCoefficientUnit.watt_per_kelvin_per_meter_squared,
        title="CombinedNonEvaporativeHeatTransferCoefficientUnit",
    )



class InverseAmountOfSubstanceUnit(UnitEnum):
    per_mole = "Item:OSW7b8304e9935651c7a91b9d5b8f6594e3"


class InverseAmountOfSubstance(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseAmountOfSubstance'
    """

    type: Optional[Any] = ["Category:OSW03376cde4b36580a9a9f6290fb6340af"]
    unit: Optional[InverseAmountOfSubstanceUnit] = Field(
        InverseAmountOfSubstanceUnit.per_mole, title="InverseAmountOfSubstanceUnit"
    )



class InverseVolumeUnit(UnitEnum):
    per_meter_cubed = "Item:OSW22ea6fd32be65173b6ce52e47446c8ed"
    per_milli_meter_cubed = (
        "Item:OSW22ea6fd32be65173b6ce52e47446c8ed#OSWd3bd49d926475edfbe5b54108429d801"
    )
    per_centi_meter_cubed = (
        "Item:OSW22ea6fd32be65173b6ce52e47446c8ed#OSWf6d64151fc835995b48c0fc8bb64a36a"
    )


class InverseVolume(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseVolume'
    """

    type: Optional[Any] = ["Category:OSWdc5df784e44e5802beda722786fd75bf"]
    unit: Optional[InverseVolumeUnit] = Field(
        InverseVolumeUnit.per_meter_cubed, title="InverseVolumeUnit"
    )



class MagneticReluctivityUnit(UnitEnum):
    per_meter_per_tesla = "Item:OSWdedbe50d76c75dc2a87b1000faa99b10"


class MagneticReluctivity(QuantityValue):
    """
    Length Per Unit Magnetic Flux is the the resistance of a material to the establishment of a magnetic field in it. It is the reciprocal of Magnetic Permeability, the inverse of the measure of the ability of a material to support the formation of a magnetic field within itself.
    """

    type: Optional[Any] = ["Category:OSW4b028ad352e557d0b10e8ab1735f03c2"]
    unit: Optional[MagneticReluctivityUnit] = Field(
        MagneticReluctivityUnit.per_meter_per_tesla, title="MagneticReluctivityUnit"
    )



class PressureCoefficientUnit(UnitEnum):
    pascal_per_kelvin = "Item:OSWac77b78c88875d4b829975141f651b94"
    mega_pascal_per_kelvin = (
        "Item:OSWac77b78c88875d4b829975141f651b94#OSW3232f6c70da55b8aa7b7c2ea4f84565b"
    )
    hecto_pascal_per_kelvin = (
        "Item:OSWac77b78c88875d4b829975141f651b94#OSW56eb00ee243c5f2993c44c2259217fd3"
    )
    kilo_pascal_per_kelvin = (
        "Item:OSWac77b78c88875d4b829975141f651b94#OSWb436256689755bf1993955ab270253c3"
    )


class PressureCoefficient(QuantityValue):
    """
    This is an autogenerated partial class definition of 'PressureCoefficient'
    """

    type: Optional[Any] = ["Category:OSWa1c670ea697d58d88f1a79b2c8aca63e"]
    unit: Optional[PressureCoefficientUnit] = Field(
        PressureCoefficientUnit.pascal_per_kelvin, title="PressureCoefficientUnit"
    )



class VaporPermeability(QuantityValue):
    """
    A material's "permeance", is dependent on thickness much like the R-value in heat transmission. Dividing the permeability of a material by its thickness gives the material's permeance. Permeance is the number that should be used to compare various products in regard to moisture transmission resistance.
    """

    type: Optional[Any] = ["Category:OSW0f0eccb9699655f58a52b9dcf741676b"]
    unit: Optional[VaporPermeabilityUnit] = Field(
        VaporPermeabilityUnit.kilo_gram_per_meter_per_pascal_per_second,
        title="VaporPermeabilityUnit",
    )



class MassConcentrationRateOfChangeUnit(UnitEnum):
    micro_gram_per_day_per_liter = "Item:OSW9108816e33465625bcd9b4850d64cf9a"


class MassConcentrationRateOfChange(QuantityValue):
    """
    the rate at which a specific chemical element or compound changes concentration over time, where with concentration expressed as mass per volume. SI unit is kg * m-3 * s-1
    """

    type: Optional[Any] = ["Category:OSW31f4583f8b095de5be781a7ced0b8117"]
    unit: Optional[MassConcentrationRateOfChangeUnit] = Field(
        MassConcentrationRateOfChangeUnit.micro_gram_per_day_per_liter,
        title="MassConcentrationRateOfChangeUnit",
    )



class MagneticFluxUnit(UnitEnum):
    weber = "Item:OSW7f1fb9d6ddeb5fb7a8a39067553a6dc1"
    milli_weber = (
        "Item:OSW7f1fb9d6ddeb5fb7a8a39067553a6dc1#OSWa09dcefcc2be5cb1ae116d0189c300e3"
    )


class MagneticFlux(QuantityValue):
    """
    "Magnetic Flux" is the product of the average magnetic field times the perpendicular area that it penetrates.
    """

    type: Optional[Any] = ["Category:OSW82a515de9bcc5af8a2f33974e7ec0f1a"]
    unit: Optional[MagneticFluxUnit] = Field(
        MagneticFluxUnit.weber, title="MagneticFluxUnit"
    )



class ActionUnit(UnitEnum):
    joule_second = "Item:OSWf045a04750e15ea2b152fb3bfebf162a"
    atto_joule_second = (
        "Item:OSWf045a04750e15ea2b152fb3bfebf162a#OSW3eaa66dd20f856fe9a5c4199bc0a1ea4"
    )


class Action(QuantityValue):
    """
    An action is usually an integral over time. But for action pertaining to fields, it may be integrated over spatial variables as well. In some cases, the action is integrated along the path followed by the physical system.  If the action is represented as an integral over time, taken a the path of the system between the initial time and the final time of the development of the system.
    The evolution of a physical system between two states is determined by requiring the action be minimized or, more generally, be stationary for small perturbations about the true evolution. This requirement leads to differential equations that describe the true evolution. Conversely, an action principle is a method for reformulating differential equations of motion for a physical system as an equivalent integral equation. Although several variants have been defined (see below), the most commonly used action principle is Hamilton's principle.
    """

    type: Optional[Any] = ["Category:OSW6a2c83eb813354edace5e2d9ead479b9"]
    unit: Optional[ActionUnit] = Field(ActionUnit.joule_second, title="ActionUnit")



class FluxUnit(UnitEnum):
    per_meter_squared_per_second = "Item:OSW580b455ce69e57418303f409d43f373a"


class Flux(QuantityValue):
    """
    Flux describes any effect that appears to pass or travel (whether it actually moves or not) through a surface or substance. [Wikipedia]
    """

    type: Optional[Any] = ["Category:OSW676564fe1a3456cda95a12cec7c2ce9e"]
    unit: Optional[FluxUnit] = Field(
        FluxUnit.per_meter_squared_per_second, title="FluxUnit"
    )



class SoundPowerLevelUnit(UnitEnum):
    byte = "Item:OSW20ac6724f1a05ee884222d546955e78f"


class SoundPowerLevel(QuantityValue):
    """
    Sound Power Level abbreviated as $SWL$ expresses sound power more practically as a relation to the threshold of hearing - 1 picoW - in a logarithmic scale.
    """

    type: Optional[Any] = ["Category:OSW7f56c0dadee65455b206ddbb22bb84f8"]
    unit: Optional[SoundPowerLevelUnit] = Field(
        SoundPowerLevelUnit.byte, title="SoundPowerLevelUnit"
    )



class TorqueUnit(UnitEnum):
    meter_newton = "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3"
    deci_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW83f4a238c5875e3587f45071e11aaaa3"
    )
    centi_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSWb7de5ae5a2f05221be05e0bf2aa74cb9"
    )
    meter_milli_newton = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW62f7907222b855ffb1920944af234145"
    )
    kilo_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSWba8c33e36b605a5083b4d9f87e89d04a"
    )
    meter_micro_newton = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSWcc1060f0faed597fbef0006b2c6de73d"
    )
    mega_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW48e50fcb919e57d99158eb2308baed11"
    )
    centi_meter_newton = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW4a6a4e3488695755a9b81d0947b0f85a"
    )


class Torque(QuantityValue):
    """
    In physics, a torque ($\tau$) is a vector that measures the tendency of a force to rotate an object about some axis. The magnitude of a torque is defined as force times its lever arm. Just as a force is a push or a pull, a torque can be thought of as a twist. The SI unit for torque is newton meters ($N m$). In U.S. customary units, it is measured in foot pounds (ft lbf) (also known as "pounds feet").
    Mathematically, the torque on a particle (which has the position r in some reference frame) can be defined as the cross product: $τ = r x F$
    where,
    r is the particle's position vector relative to the fulcrum
    F is the force acting on the particles,
    or, more generally, torque can be defined as the rate of change of angular momentum: $τ = dL/dt$
    where,
    L is the angular momentum vector
    t stands for time.
    """

    type: Optional[Any] = ["Category:OSW77f25284632d50b0ae2be064592412ce"]
    unit: Optional[TorqueUnit] = Field(TorqueUnit.meter_newton, title="TorqueUnit")



class TotalLinearStoppingPowerUnit(UnitEnum):
    joule_per_meter = "Item:OSW0505357de255592eb766bdfce883acb3"


class TotalLinearStoppingPower(QuantityValue):
    """
    The "Total Linear Stopping Power" is defined as the average energy loss of the particle per unit path length.
    """

    type: Optional[Any] = ["Category:OSWd95e7eb103785c8597c8cd21e96c3c86"]
    unit: Optional[TotalLinearStoppingPowerUnit] = Field(
        TotalLinearStoppingPowerUnit.joule_per_meter,
        title="TotalLinearStoppingPowerUnit",
    )



class TemporalSummationFunctionUnit(UnitEnum):
    per_second_per_steradian = "Item:OSWaf6c62c0856f5ac288ac862f5344f227"


class TemporalSummationFunction(QuantityValue):
    """
    "Temporal Summation Function" is the ability of the human eye to produce a composite signal from the signals coming into an eye during a short time interval.
    """

    type: Optional[Any] = ["Category:OSW85210337b1045b7286972e73a44c6e1b"]
    unit: Optional[TemporalSummationFunctionUnit] = Field(
        TemporalSummationFunctionUnit.per_second_per_steradian,
        title="TemporalSummationFunctionUnit",
    )



class LagrangeFunctionUnit(UnitEnum):
    joule = "Item:OSW730568cd7ae65906abbbcef1d15cb074"
    peta_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW4e7003f5d7ff58a190167711dd63b0bd"
    )
    kilo_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWad2518d42b685f569679c3599455c3d3"
    )
    milli_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW6df751011258508e9d15967190c819f3"
    )
    femto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW2d5cdc08b064506e8f9a5b0456b7a0b3"
    )
    tera_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW0ac3643d930d5c99936e5ece487a9634"
    )
    exa_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW5ba80670b2945c08b35551442d3169d5"
    )
    giga_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc26bf1cf449d56ef8122745336585d2b"
    )
    mega_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc1525b1f1fc05c40b9715328bf707805"
    )
    atto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWa73c696efa58519aa07c265ea965ceda"
    )


class LagrangeFunction(QuantityValue):
    """
    The Lagrange Function is a function that summarizes the dynamics of the system.
    """

    type: Optional[Any] = ["Category:OSW81ed93909dda56e5a0a9a1996449f082"]
    unit: Optional[LagrangeFunctionUnit] = Field(
        LagrangeFunctionUnit.joule, title="LagrangeFunctionUnit"
    )



class SectionModulusUnit(UnitEnum):
    meter_cubed = "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8"
    milli_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSWa9d92cf2bcb95b1887a23f99b51d8d36"
    )
    deca_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSW5024fe1a02365460bbc23fa2e8a46a7b"
    )
    micro_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSW7126d9f54e0b565898ccf21988c04366"
    )
    centi_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSWcd2df951f11a56d2a06705a8f16b0662"
    )
    deci_meter_cubed = (
        "Item:OSW7aa0d48fa4a45427a03c5abd43b488f8#OSWdda7ee9dea455958af1466a861d5bf7d"
    )


class SectionModulus(QuantityValue):
    """
    The Section Modulus is a geometric property for a given cross-section used in the design of beams or flexural members.
    """

    type: Optional[Any] = ["Category:OSW6431223a253052b98a72e63b4f62ca09"]
    unit: Optional[SectionModulusUnit] = Field(
        SectionModulusUnit.meter_cubed, title="SectionModulusUnit"
    )



class ViscosityUnit(UnitEnum):
    pascal_second = "Item:OSWfb230f7ff1a55c23accf8ae94aacc9e1"
    milli_pascal_second = (
        "Item:OSWfb230f7ff1a55c23accf8ae94aacc9e1#OSW8e1783ac9f0b5fe3b404dcfbce8940cb"
    )


class Viscosity(QuantityValue):
    """
    Viscosity is a measure of the resistance of a fluid which is being deformed by either shear stress or extensional stress. In general terms it is the resistance of a liquid to flow, or its "thickness". Viscosity describes a fluid's internal resistance to flow and may be thought of as a measure of fluid friction. [Wikipedia]. In general conversation or in non-scientific contexts, if someone refers to the viscosity of a fluid, they're likely talking about its dynamic (or absolute) viscosity. However, in engineering or scientific contexts, it's essential to clarify which type of viscosity is being discussed, as the interpretation and use of the data may differ depending on whether one is talking about dynamic or kinematic viscosity.
    """

    type: Optional[Any] = ["Category:OSWed71b6bba4a758b5b10082861ad0ea44"]
    unit: Optional[ViscosityUnit] = Field(
        ViscosityUnit.pascal_second, title="ViscosityUnit"
    )



class InversePressureUnit(UnitEnum):
    per_pascal = "Item:OSWf030abd4441d52a7a8c5f84950985ea4"


class InversePressure(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InversePressure'
    """

    type: Optional[Any] = ["Category:OSWdd95fa0b1f0b5917acc7e3aa22585ebc"]
    unit: Optional[InversePressureUnit] = Field(
        InversePressureUnit.per_pascal, title="InversePressureUnit"
    )



class DensityOfStatesUnit(UnitEnum):
    second_per_meter_cubed_per_radian = "Item:OSW8d374d57d51f52fd9f4fae71895deb07"


class DensityOfStates(QuantityValue):
    """
    "Density of States" is the number of vibrational modes in an infinitesimal interval of angular frequency divided by the range of that interval and by volume.
    """

    type: Optional[Any] = ["Category:OSWa37f106768d4575abdb567b17d904d2d"]
    unit: Optional[DensityOfStatesUnit] = Field(
        DensityOfStatesUnit.second_per_meter_cubed_per_radian,
        title="DensityOfStatesUnit",
    )



class BulkModulusUnit(UnitEnum):
    pascal = "Item:OSWb663e6bff3595e7b93b28fffce66c50c"
    giga_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW49bb4743a5735e189777f3c6bd422a52"
    )
    deca_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW8d40059d9e3951bb97378fe3f119ba21"
    )
    milli_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW38b0e12539b05ce28cd126c8eea29f95"
    )
    mega_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW0ec5bf8132b25e58b7032766bd9b3225"
    )
    kilo_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW264ebdc21f54568593a91bbd832b6fbf"
    )
    hecto_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW482939f123595314beca39ad32d65a15"
    )
    micro_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW5def4be309ce50ee933c99cf4b74e310"
    )


class BulkModulus(QuantityValue):
    """
    The bulk modulus of a substance measures the substance's resistance to uniform compression. It is defined as the ratio of the infinitesimal pressure increase to the resulting relative decrease of the volume.
    """

    type: Optional[Any] = ["Category:OSW1c930bb324ca5e5b84c25be2079b2d21"]
    unit: Optional[BulkModulusUnit] = Field(
        BulkModulusUnit.pascal, title="BulkModulusUnit"
    )



class SpectralAngularCrossSectionUnit(UnitEnum):
    meter_squared_per_joule_per_steradian = "Item:OSW67a27e9bd9685e61a525f06b3e25b81f"


class SpectralAngularCrossSection(QuantityValue):
    """
    "Spectral Angular Cross-section" is the cross-section for ejecting or scattering a particle into an elementary cone with energy $E$ in an energy interval, divided by the solid angle $d\Omega$ of that cone and the range $dE$ of that interval.
    """

    type: Optional[Any] = ["Category:OSW4e1cadc179b355b39ed40a4ea0c3ff5a"]
    unit: Optional[SpectralAngularCrossSectionUnit] = Field(
        SpectralAngularCrossSectionUnit.meter_squared_per_joule_per_steradian,
        title="SpectralAngularCrossSectionUnit",
    )



class MolarEnergyUnit(UnitEnum):
    joule_per_mole = "Item:OSW7e66beeef6b05637a554d3506d689000"
    kilo_joule_per_mole = (
        "Item:OSW7e66beeef6b05637a554d3506d689000#OSW23b10a54326955adb1862933713551f9"
    )


class MolarEnergy(QuantityValue):
    """
    "Molar Energy" is the total energy contained by a thermodynamic system. The unit is $$J/mol$$, also expressed as $$joule/mole$$,  or $$joules per mole$$. This unit is commonly used in the SI unit system. The quantity has the dimension of $$M \cdot L^2 \cdot  T^{-2} \cdot N^{-1}$$ where $$M$$ is mass, $$L$$ is length, $$T$$ is time, and $$N$$ is amount of substance.
    """

    type: Optional[Any] = ["Category:OSW21ec5968e3c2533d98f20564838541fa"]
    unit: Optional[MolarEnergyUnit] = Field(
        MolarEnergyUnit.joule_per_mole, title="MolarEnergyUnit"
    )



class LinearMomentumUnit(UnitEnum):
    newton_second = "Item:OSWb05df920a96b5987aeb46a9b4f7ca333"


class LinearMomentum(QuantityValue):
    """
    Linear momentum is the quantity obtained by multiplying the mass of a body by its linear velocity. The momentum of a continuous medium is given by the integral of the velocity over the mass of the medium or by the product of the total mass of the medium and the velocity of the center of gravity of the medium.The SI unit for linear momentum is meter-kilogram per second ($m-kg/s$).
    """

    type: Optional[Any] = ["Category:OSW22f40c87ac435474b8525e7268e7ca01"]
    unit: Optional[LinearMomentumUnit] = Field(
        LinearMomentumUnit.newton_second, title="LinearMomentumUnit"
    )



class ElectromagneticWavePhaseSpeedUnit(UnitEnum):
    meter_per_second = "Item:OSW78331234e1a15aeebd8b0caa71201939"
    centi_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWd094e4cfd62c52248aad5ef87c19fb7d"
    )
    micro_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWfc9fca27ba5b543c8780521b4af39189"
    )
    milli_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW4937ac85021f506cb7ba3958f2216bd1"
    )
    kilo_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW9f12ce12bc725cd59791265e2e480fd2"
    )


class ElectromagneticWavePhaseSpeed(QuantityValue):
    """
    "Electromagnetic Wave Phase Speed" is the ratio of angular velocity and wavenumber.
    """

    type: Optional[Any] = ["Category:OSW0e2b889bd54e5b7da3c2e14c3c4b39ab"]
    unit: Optional[ElectromagneticWavePhaseSpeedUnit] = Field(
        ElectromagneticWavePhaseSpeedUnit.meter_per_second,
        title="ElectromagneticWavePhaseSpeedUnit",
    )



class SpecificHeatCapacityUnit(UnitEnum):
    meter_squared_per_kelvin_per_second_squared = (
        "Item:OSW3b1e36710511523da37025a70b6a305d"
    )


class SpecificHeatCapacity(QuantityValue):
    """
    Specific Heat Capacity of a solid or liquid is defined as the heat required to raise unit mass of substance by one degree of temperature. This is Heat Capacity divided by Mass. Note that there are corresponding molar quantities.
    """

    type: Optional[Any] = ["Category:OSW8fa2469531415841b65412f705d138d6"]
    unit: Optional[SpecificHeatCapacityUnit] = Field(
        SpecificHeatCapacityUnit.meter_squared_per_kelvin_per_second_squared,
        title="SpecificHeatCapacityUnit",
    )



class LuminousEnergyUnit(UnitEnum):
    lumen_second = "Item:OSWc4c970d2dd145fbc883dfca4b380edff"


class LuminousEnergy(QuantityValue):
    """
    Luminous Energy is the perceived energy of light. This is sometimes also called the quantity of light.
    """

    type: Optional[Any] = ["Category:OSWdcee8dd4e72258d5abb828567c3e7a0c"]
    unit: Optional[LuminousEnergyUnit] = Field(
        LuminousEnergyUnit.lumen_second, title="LuminousEnergyUnit"
    )



class ResistivityUnit(UnitEnum):
    meter_ohm = "Item:OSW825f941d934e5a73866e39b6c42c99f0"


class Resistivity(QuantityValue):
    """
    "Resistivity" is the inverse of the conductivity when this inverse exists.
    """

    type: Optional[Any] = ["Category:OSW25cb564bcaed56bc84bcb4c518f7d8d8"]
    unit: Optional[ResistivityUnit] = Field(
        ResistivityUnit.meter_ohm, title="ResistivityUnit"
    )



class ModulusOfImpedanceUnit(UnitEnum):
    ohm = "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1"
    kilo_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5e05beabf6935ae2b559c1cffc788110"
    )
    milli_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWa8d17cb3f4255320af6052cbd471d716"
    )
    tera_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5196e38637c752e58c2b5be5521e4234"
    )
    giga_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW66dbbd77c6ca5d5684b223fdfcc7b773"
    )
    mega_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW14b14dd3c32d5ee199a67e3796734a4a"
    )
    micro_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWacd4090bd8335717b6eea6b8c1151b29"
    )


class ModulusOfImpedance(QuantityValue):
    """
    "Modulus Of Impedance} is the absolute value of the quantity $\textit{impedance}$. Apparent impedance is defined more generally as

    the quotient of rms voltage and rms electric current; it is often denoted by $Z$.
    """

    type: Optional[Any] = ["Category:OSW4804fb4f11345ebe99f0eaaabafc1c88"]
    unit: Optional[ModulusOfImpedanceUnit] = Field(
        ModulusOfImpedanceUnit.ohm, title="ModulusOfImpedanceUnit"
    )



class WaterVapourDiffusionCoefficientUnit(UnitEnum):
    kilo_gram_per_meter_per_pascal_per_second = (
        "Item:OSWa2b4ab78b9975e0891d0d14dfbb12314"
    )


class WaterVapourDiffusionCoefficient(QuantityValue):
    """
    The Water vapour diffusion coefficient describes how easy vapor diffusion happens in a given material.
    """

    type: Optional[Any] = ["Category:OSW31d75c6ae9295c32926357387234c870"]
    unit: Optional[WaterVapourDiffusionCoefficientUnit] = Field(
        WaterVapourDiffusionCoefficientUnit.kilo_gram_per_meter_per_pascal_per_second,
        title="WaterVapourDiffusionCoefficientUnit",
    )



class VolumetricHeatCapacityUnit(UnitEnum):
    joule_per_kelvin_per_meter_cubed = "Item:OSW4db6d50e4e4e5d9dbd549d706e3f6c44"
    joule_per_centi_meter_cubed_per_kelvin = (
        "Item:OSW4db6d50e4e4e5d9dbd549d706e3f6c44#OSW831c2e0119cd5e46a75afc834fffaf7d"
    )


class VolumetricHeatCapacity(QuantityValue):
    """
    $\textit{Volumetric Heat Capacity (VHC)}$, also termed $\textit{volume-specific heat capacity}$, describes the ability of a given volume of a substance to store internal energy while undergoing a given temperature change, but without undergoing a phase transition. It is different from specific heat capacity in that the VHC is a $\textit{per unit volume}$ measure of the relationship between thermal energy and temperature of a material, while the specific heat is a $\textit{per unit mass}$ measure (or occasionally per molar quantity of the material).
    """

    type: Optional[Any] = ["Category:OSW9eb931426c785245bf64c1fe1dce25c8"]
    unit: Optional[VolumetricHeatCapacityUnit] = Field(
        VolumetricHeatCapacityUnit.joule_per_kelvin_per_meter_cubed,
        title="VolumetricHeatCapacityUnit",
    )



class WarpingMomentUnit(UnitEnum):
    meter_squared_newton = "Item:OSW9dfac70a65b753709e52cb3591dd8547"
    kilo_newton_meter_squared = (
        "Item:OSW9dfac70a65b753709e52cb3591dd8547#OSW54ba1a65b3a75b708a5ddb4089c205b1"
    )


class WarpingMoment(QuantityValue):
    """
    The warping moment measure is a measure for the warping moment, which occurs in warping torsional analysis. It is usually measured in kNm².
    """

    type: Optional[Any] = ["Category:OSW9a57ea5fa37f59cfa4eb6ad9d2427c4e"]
    unit: Optional[WarpingMomentUnit] = Field(
        WarpingMomentUnit.meter_squared_newton, title="WarpingMomentUnit"
    )



class CoefficientOfHeatTransferUnit(UnitEnum):
    watt_per_kelvin_per_meter_squared = "Item:OSWdc31cad7e9225defbc08f6f79bf5c4ea"


class CoefficientOfHeatTransfer(QuantityValue):
    """
    "Coefficient of Heat Transfer", in thermodynamics and in mechanical and chemical engineering, is used in calculating the heat transfer, typically by convection or phase transition between a fluid and a solid. The heat transfer coefficient is the proportionality coefficient between the heat flux, that is heat flow per unit area, q/A, and the thermodynamic driving force for the flow of heat (that is, the temperature difference, (Delta T).  Areic heat flow rate divided by thermodynamic temperature difference. In building technology, the "Coefficient of Heat Transfer", is often called "thermal transmittance}" with the symbol "U". It has SI units in watts per squared meter kelvin.
    """

    type: Optional[Any] = ["Category:OSW46cf5d4e08e25909a1bbad7563535a8e"]
    unit: Optional[CoefficientOfHeatTransferUnit] = Field(
        CoefficientOfHeatTransferUnit.watt_per_kelvin_per_meter_squared,
        title="CoefficientOfHeatTransferUnit",
    )



class ExtentOfReactionUnit(UnitEnum):
    mole = "Item:OSW4d9412cede875e399cffb35415646316"
    milli_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSW09461c4b2fa85ab683a3572a199ef16b"
    )
    kilo_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSW2971b3cb7eca516184282ecfa45bfb81"
    )
    femto_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSWb4b00897b51e505a8c8cac8d6958b73b"
    )
    micro_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSW1d4f11a4a1425dba81c9dac510278967"
    )


class ExtentOfReaction(QuantityValue):
    """
    In physical chemistry, the "Extent of Reaction" is a quantity that measures the extent in which the reaction proceeds.
    """

    type: Optional[Any] = ["Category:OSW8961f38102645fbbbd5a925157d7ab9e"]
    unit: Optional[ExtentOfReactionUnit] = Field(
        ExtentOfReactionUnit.mole, title="ExtentOfReactionUnit"
    )



class DiffusionCoefficient(QuantityValue):
    """
    The "Diffusion Coefficient" is a proportionality constant between the molar flux due to molecular diffusion and the gradient in the concentration of the species (or the driving force for diffusion). Diffusivity is encountered in Fick's law and numerous other equations of physical chemistry.
    """

    type: Optional[Any] = ["Category:OSW9f693a8e95ec59248b109c678328b872"]
    unit: Optional[DiffusionCoefficientUnit] = Field(
        DiffusionCoefficientUnit.meter_squared_per_second,
        title="DiffusionCoefficientUnit",
    )



class ExchangeIntegralUnit(UnitEnum):
    joule = "Item:OSW730568cd7ae65906abbbcef1d15cb074"
    peta_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW4e7003f5d7ff58a190167711dd63b0bd"
    )
    kilo_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWad2518d42b685f569679c3599455c3d3"
    )
    milli_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW6df751011258508e9d15967190c819f3"
    )
    femto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW2d5cdc08b064506e8f9a5b0456b7a0b3"
    )
    tera_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW0ac3643d930d5c99936e5ece487a9634"
    )
    exa_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW5ba80670b2945c08b35551442d3169d5"
    )
    giga_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc26bf1cf449d56ef8122745336585d2b"
    )
    mega_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc1525b1f1fc05c40b9715328bf707805"
    )
    atto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWa73c696efa58519aa07c265ea965ceda"
    )


class ExchangeIntegral(QuantityValue):
    """
    "Exchange Integral" is the constituent of the interaction energy between the spins of adjacent electrons in matter arising from the overlap of electron state functions.
    """

    type: Optional[Any] = ["Category:OSWe45b76ea9ca85972997b6808b31b3b92"]
    unit: Optional[ExchangeIntegralUnit] = Field(
        ExchangeIntegralUnit.joule, title="ExchangeIntegralUnit"
    )



class VentilationRatePerFloorAreaUnit(UnitEnum):
    liter_per_meter_squared_per_second = "Item:OSW3248fcac4b1b514b81d2b9f7bf05e180"


class VentilationRatePerFloorArea(QuantityValue):
    """
    Ventilation Rate is often expressed by the volumetric flowrate of outdoor air introduced to a building. However, ASHRAE now recommends ventilation rates dependent upon floor area.
    """

    type: Optional[Any] = ["Category:OSW8cf0ce0f6ab85ec7b70b73d8f79577cd"]
    unit: Optional[VentilationRatePerFloorAreaUnit] = Field(
        VentilationRatePerFloorAreaUnit.liter_per_meter_squared_per_second,
        title="VentilationRatePerFloorAreaUnit",
    )



class AreaAngleUnit(UnitEnum):
    meter_squared_steradian = "Item:OSW9f81b80e2dfd530c98579b65285d4f20"


class AreaAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'AreaAngle'
    """

    type: Optional[Any] = ["Category:OSWada455630bff528dbbf65f20a630212b"]
    unit: Optional[AreaAngleUnit] = Field(
        AreaAngleUnit.meter_squared_steradian, title="AreaAngleUnit"
    )



class AreaThermalExpansionUnit(UnitEnum):
    meter_squared_per_kelvin = "Item:OSWf1731214810f50999e9ce8343fe57e34"


class AreaThermalExpansion(QuantityValue):
    """
    When the temperature of a substance changes, the energy that is stored in the intermolecular bonds between atoms changes. When the stored energy increases, so does the length of the molecular bonds. As a result, solids typically expand in response to heating and contract on cooling; this dimensional response to temperature change is expressed by its coefficient of thermal expansion.
    """

    type: Optional[Any] = ["Category:OSW1ad6b428ff385d10b28bdc0221bf5b81"]
    unit: Optional[AreaThermalExpansionUnit] = Field(
        AreaThermalExpansionUnit.meter_squared_per_kelvin,
        title="AreaThermalExpansionUnit",
    )



class InverseLengthUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class InverseLength(QuantityValue):
    """
    Reciprocal length or inverse length is a measurement used in several branches of science and mathematics. As the reciprocal of length, common units used for this measurement include the reciprocal metre or inverse metre ($m^{-1}$), the reciprocal centimetre or inverse centimetre ($cm^{-1}$), and, in optics, the dioptre.
    """

    type: Optional[Any] = ["Category:OSW23837e2c50f05ba884682b08465bf173"]
    unit: Optional[InverseLengthUnit] = Field(
        InverseLengthUnit.per_meter, title="InverseLengthUnit"
    )



class LuminousIntensityUnit(UnitEnum):
    candela = "Item:OSWf04f81ce6d6a53b98630967e75958e53"


class LuminousIntensity(QuantityValue):
    """
    Luminous Intensity is a measure of the wavelength-weighted power emitted by a light source in a particular direction per unit solid angle. The weighting is determined by the luminosity function, a standardized model of the sensitivity of the human eye to different wavelengths.
    """

    type: Optional[Any] = ["Category:OSWcd5084e98d8a541eb5d121ae983fad3d"]
    unit: Optional[LuminousIntensityUnit] = Field(
        LuminousIntensityUnit.candela, title="LuminousIntensityUnit"
    )



class VolumeThermalExpansionUnit(UnitEnum):
    meter_cubed_per_kelvin = "Item:OSWb9f55dd232415132bdf9e63794052746"
    centi_meter_cubed_per_kelvin = (
        "Item:OSWb9f55dd232415132bdf9e63794052746#OSW554b5cf2e310542f848f9522a4f34f70"
    )


class VolumeThermalExpansion(QuantityValue):
    """
    When the temperature of a substance changes, the energy that is stored in the intermolecular bonds between atoms changes. When the stored energy increases, so does the length of the molecular bonds. As a result, solids typically expand in response to heating and contract on cooling; this dimensional response to temperature change is expressed by its coefficient of thermal expansion.

    Different coefficients of thermal expansion can be defined for a substance depending on whether the expansion is measured by:

        * linear thermal expansion
        * area thermal expansion
        * volumetric thermal expansion

    These characteristics are closely related. The volumetric thermal expansion coefficient can be defined for both liquids and solids. The linear thermal expansion can only be defined for solids, and is common in engineering applications.

    Some substances expand when cooled, such as freezing water, so they have negative thermal expansion coefficients. [Wikipedia]
    """

    type: Optional[Any] = ["Category:OSWfa99fdcfe84d5a008472386406ac1416"]
    unit: Optional[VolumeThermalExpansionUnit] = Field(
        VolumeThermalExpansionUnit.meter_cubed_per_kelvin,
        title="VolumeThermalExpansionUnit",
    )



class SoundPressureLevelUnit(UnitEnum):
    byte = "Item:OSW20ac6724f1a05ee884222d546955e78f"


class SoundPressureLevel(QuantityValue):
    """
    Sound pressure level ($SPL$) or sound level is a logarithmic measure of the effective sound pressure of a sound relative to a reference value. It is measured in decibels (dB) above a standard reference level.
    """

    type: Optional[Any] = ["Category:OSW002d158549e955bea02a7c957b139a60"]
    unit: Optional[SoundPressureLevelUnit] = Field(
        SoundPressureLevelUnit.byte, title="SoundPressureLevelUnit"
    )



class CompressibilityUnit(UnitEnum):
    meter_squared_per_newton = "Item:OSWfabd2eabe9d5542f9de724b3d10058ec"


class Compressibility(QuantityValue):
    """
    Compressibility is a measure of the relative volume change of a fluid or solid as a response to a pressure (or mean stress) change.
    """

    type: Optional[Any] = ["Category:OSWe98ffe7d93775d5eae95108872432f2f"]
    unit: Optional[CompressibilityUnit] = Field(
        CompressibilityUnit.meter_squared_per_newton, title="CompressibilityUnit"
    )



class PhotosyntheticPhotonFluxUnit(UnitEnum):
    mole_per_second = "Item:OSW6b764c5799c45b62bb947ed93f8b99eb"
    micro_mole_per_second = (
        "Item:OSW6b764c5799c45b62bb947ed93f8b99eb#OSW10e98cb9b70150158fc1544d9f094ad2"
    )
    kilo_mole_per_second = (
        "Item:OSW6b764c5799c45b62bb947ed93f8b99eb#OSWb3ad32c2d89057e08a13a3562b52bd17"
    )


class PhotosyntheticPhotonFlux(QuantityValue):
    """
    Photosynthetic Photon Flux (PPF) is a measurement of the total number of photons emitted by a light source each second within the PAR wavelength range and is measured in μmol/s. Lighting manufacturers may specify their grow light products in terms of PPF. It can be considered as analogous to measuring the luminous flux (lumens) of visible light which would typically require the use of an integrating sphere or a goniometer system with spectroradiometer sensor.
    """

    type: Optional[Any] = ["Category:OSW6daf9ac4c6f859fbb5f6e241f1430f09"]
    unit: Optional[PhotosyntheticPhotonFluxUnit] = Field(
        PhotosyntheticPhotonFluxUnit.mole_per_second,
        title="PhotosyntheticPhotonFluxUnit",
    )



class MolarOpticalRotatoryPowerUnit(UnitEnum):
    meter_squared_radian_per_mole = "Item:OSW6e91dd70b9f75580bdb3d962228cb99b"


class MolarOpticalRotatoryPower(QuantityValue):
    """
    The "Molar Optical Rotatory Power" Angle of optical rotation divided by the optical path length through the medium and by the amount concentration giving the molar optical rotatory power.
    """

    type: Optional[Any] = ["Category:OSWfd98416f9f0b5cb681576143d2d4ab05"]
    unit: Optional[MolarOpticalRotatoryPowerUnit] = Field(
        MolarOpticalRotatoryPowerUnit.meter_squared_radian_per_mole,
        title="MolarOpticalRotatoryPowerUnit",
    )



class ElectricQuadrupoleMomentUnit(UnitEnum):
    coulomb_meter_squared = "Item:OSW46fa6db298ce5915a82932c6e4b72085"


class ElectricQuadrupoleMoment(QuantityValue):
    """
    The Electric Quadrupole Moment is a quantity which describes the effective shape of the ellipsoid of nuclear charge distribution. A non-zero quadrupole moment Q indicates that the charge distribution is not spherically symmetric. By convention, the value of Q is taken to be positive if the ellipsoid is prolate and negative if it is oblate. In general, the electric quadrupole moment is tensor-valued.
    """

    type: Optional[Any] = ["Category:OSW7fdace54bea65a29af32ab2124bc8087"]
    unit: Optional[ElectricQuadrupoleMomentUnit] = Field(
        ElectricQuadrupoleMomentUnit.coulomb_meter_squared,
        title="ElectricQuadrupoleMomentUnit",
    )



class SecondMomentOfAreaUnit(UnitEnum):
    field_4 = "Item:OSWe4f01fe00389574e905718a14481ed36"
    field_4_1 = (
        "Item:OSWe4f01fe00389574e905718a14481ed36#OSW73b630d93619585bbc7f4a3a4a3be104"
    )
    field_4_2 = (
        "Item:OSWe4f01fe00389574e905718a14481ed36#OSW568d0d17db6551c1993de3d51c6051cc"
    )


class SecondMomentOfArea(QuantityValue):
    """
    The second moment of area is a property of a physical object that can be used to predict its resistance to bending and deflection. The deflection of an object under load depends not only on the load, but also on the geometry of the object's cross-section.
    """

    type: Optional[Any] = ["Category:OSWbd5f31fa763d5f4b9f8be79284269e47"]
    unit: Optional[SecondMomentOfAreaUnit] = Field(
        SecondMomentOfAreaUnit.field_4, title="SecondMomentOfAreaUnit"
    )



class ElectricChargePerAmountOfSubstanceUnit(UnitEnum):
    coulomb_per_mole = "Item:OSW5296e8a9268e513a9b92690db31d7f4c"


class ElectricChargePerAmountOfSubstance(QuantityValue):
    """
    "Electric Charge Per Amount Of Substance" is the charge assocated with a given amount of substance. Un the ISO and SI systems this is $1 mol$.
    """

    type: Optional[Any] = ["Category:OSWbc5a62d98afe5e14906cac7af329389e"]
    unit: Optional[ElectricChargePerAmountOfSubstanceUnit] = Field(
        ElectricChargePerAmountOfSubstanceUnit.coulomb_per_mole,
        title="ElectricChargePerAmountOfSubstanceUnit",
    )



class VoltageUnit(UnitEnum):
    volt = "Item:OSW85efe1428cb75363a75aab6435e2d98d"
    milli_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW82d25d00b1485cc18c204f95de4536a9"
    )
    micro_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSWc0cb09a94aa553589a59ea70bfccfc96"
    )
    kilo_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW4deed980237a5360b48e0dd1331d4199"
    )
    mega_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW78798aa1bdcb57f0aea8d4eb86ff3355"
    )


class Voltage(QuantityValue):
    """
    $\textit{Voltage}$, also referred to as $\textit{Electric Tension}$, is the difference between electrical potentials of two points. For an electric field within a medium, $U_{ab} = - \int_{r_a}^{r_b} E . {dr}$, where $E$ is electric field strength.
    For an irrotational electric field, the voltage is independent of the path between the two points $a$ and $b$.
    """

    type: Optional[Any] = ["Category:OSW19bdaead0e9852b68da79f45423f2b58"]
    unit: Optional[VoltageUnit] = Field(VoltageUnit.volt, title="VoltageUnit")



class MolarFlowRateUnit(UnitEnum):
    mole_per_second = "Item:OSW6b764c5799c45b62bb947ed93f8b99eb"
    micro_mole_per_second = (
        "Item:OSW6b764c5799c45b62bb947ed93f8b99eb#OSW10e98cb9b70150158fc1544d9f094ad2"
    )
    kilo_mole_per_second = (
        "Item:OSW6b764c5799c45b62bb947ed93f8b99eb#OSWb3ad32c2d89057e08a13a3562b52bd17"
    )


class MolarFlowRate(QuantityValue):
    """
    Molar Flow Rate is a measure of the amount of substance (the number of molecules) that passes through a given area perpendicular to the flow in a given time. Typically this area is constrained, for example a section through a pipe, but it could also apply to an open flow.
    """

    type: Optional[Any] = ["Category:OSW1ccf7d20cba95e54a9c0b3f6c9ca2c6b"]
    unit: Optional[MolarFlowRateUnit] = Field(
        MolarFlowRateUnit.mole_per_second, title="MolarFlowRateUnit"
    )



class SeebeckCoefficientUnit(UnitEnum):
    volt_per_kelvin = "Item:OSW8998763d58065a069429e7e6fe3c153a"


class SeebeckCoefficient(QuantityValue):
    """
    "Seebeck Coefficient", or thermopower, or thermoelectric power of a material is a measure of the magnitude of an induced thermoelectric voltage in response to a temperature difference across that material.
    """

    type: Optional[Any] = ["Category:OSWbade8d0a825f5900be44268cec649801"]
    unit: Optional[SeebeckCoefficientUnit] = Field(
        SeebeckCoefficientUnit.volt_per_kelvin, title="SeebeckCoefficientUnit"
    )



class MagneticDipoleMomentUnit(UnitEnum):
    meter_squared_newton_per_ampere = "Item:OSW164f2a6f077a564c914320ff303d09e8"


class MagneticDipoleMoment(QuantityValue):
    """
    "Magnetic Dipole Moment" is the magnetic moment of a system is a measure of the magnitude and the direction of its magnetism. Magnetic moment usually refers to its Magnetic Dipole Moment, and quantifies the contribution of the system's internal magnetism to the external dipolar magnetic field produced by the system (that is, the component of the external magnetic field that is inversely proportional to the cube of the distance to the observer). The Magnetic Dipole Moment is a vector-valued quantity. For a particle or nucleus, vector quantity causing an increment $\Delta W = -\mu \cdot B$ to its energy $W$ in an external magnetic field with magnetic flux density $B$.
    """

    type: Optional[Any] = ["Category:OSW6d902d567a1a5a89bde7cea878179186"]
    unit: Optional[MagneticDipoleMomentUnit] = Field(
        MagneticDipoleMomentUnit.meter_squared_newton_per_ampere,
        title="MagneticDipoleMomentUnit",
    )



class PermittivityUnit(UnitEnum):
    farad_per_meter = "Item:OSWe279fe2c49705948a6f2fff270d50be1"
    nano_farad_per_meter = (
        "Item:OSWe279fe2c49705948a6f2fff270d50be1#OSWa8178412351155eea5ff7170de8040be"
    )
    pico_farad_per_meter = (
        "Item:OSWe279fe2c49705948a6f2fff270d50be1#OSW635f4b8020b655738a877cb7e87831be"
    )
    farad_per_kilo_meter = (
        "Item:OSWe279fe2c49705948a6f2fff270d50be1#OSW47e4ca2649285de5b1dbd98338fac916"
    )
    micro_farad_per_meter = (
        "Item:OSWe279fe2c49705948a6f2fff270d50be1#OSWc45e1c5e49095d4d805ea836290790b7"
    )


class Permittivity(QuantityValue):
    """
    "Permittivity" is a physical quantity that describes how an electric field affects, and is affected by a dielectric medium, and is determined by the ability of a material to polarize in response to the field, and thereby reduce the total electric field inside the material.  Permittivity is often a scalar valued quantity, however in the general case it is tensor-valued.
    """

    type: Optional[Any] = ["Category:OSWa2c1b3040a2b51e7a8ebfa4524755702"]
    unit: Optional[PermittivityUnit] = Field(
        PermittivityUnit.farad_per_meter, title="PermittivityUnit"
    )



class InverseSquareTimeUnit(UnitEnum):
    per_second_squared = "Item:OSWbefab75c6042567c84545b5fab456055"


class InverseSquareTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseSquareTime'
    """

    type: Optional[Any] = ["Category:OSW3484a41e5b0e57f7998a5033177ab080"]
    unit: Optional[InverseSquareTimeUnit] = Field(
        InverseSquareTimeUnit.per_second_squared, title="InverseSquareTimeUnit"
    )



class AreaPerHeatingLoadUnit(UnitEnum):
    meter_squared_per_watt = "Item:OSWe1310c5fc4e65dc68ddc749604c7d758"
    meter_squared_per_kilo_watt = (
        "Item:OSWe1310c5fc4e65dc68ddc749604c7d758#OSW1e8006cf834952ab86733cd87ed7be1c"
    )


class AreaPerHeatingLoad(QuantityValue):
    """
    The ratio of an area and the power required for maintaining room temperature at a given level
    """

    type: Optional[Any] = ["Category:OSW4d26c25abed1595ebf6faebbb937aa29"]
    unit: Optional[AreaPerHeatingLoadUnit] = Field(
        AreaPerHeatingLoadUnit.meter_squared_per_watt, title="AreaPerHeatingLoadUnit"
    )



class DisplacementCurrentUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class DisplacementCurrent(QuantityValue):
    """
    "Displacement Current" is a quantity appearing in Maxwell's equations that is defined in terms of the rate of change of electric displacement field. Displacement current has the units of electric current density, and it has an associated magnetic field just as actual currents do. However it is not an electric current of moving charges, but a time-varying electric field. In materials, there is also a contribution from the slight motion of charges bound in atoms, dielectric polarization.
    """

    type: Optional[Any] = ["Category:OSW4a357300c6655a1b9d5d739b6dffd1fe"]
    unit: Optional[DisplacementCurrentUnit] = Field(
        DisplacementCurrentUnit.ampere, title="DisplacementCurrentUnit"
    )



class MolarMassUnit(UnitEnum):
    kilo_gram_per_mole = (
        "Item:OSW968a3fd57529500f9eb03f4efc083e36#OSW31a2c5ae09d1578a843267fef44c2cdb"
    )


class MolarMass(QuantityValue):
    """
    In chemistry, the molar mass M is defined as the mass of a given substance (chemical element or chemical compound) divided by its amount of substance. It is a physical property of a given substance. The base SI unit for molar mass is $kg/mol$.
    """

    type: Optional[Any] = ["Category:OSW57dc5920ca595bc5b7c1f41b0a79bad3"]
    unit: Optional[MolarMassUnit] = Field(
        MolarMassUnit.kilo_gram_per_mole, title="MolarMassUnit"
    )



class SoundExposureUnit(UnitEnum):
    pascal_squared_second = "Item:OSW480ba7517ec75d798c6b56f61d91de1d"


class SoundExposure(QuantityValue):
    """
    Sound Exposure is the energy of the A-weighted sound calculated over the measurement time(s). For a given period of time, an increase of 10 dB(A) in sound pressure level corresponds to a tenfold increase in E.
    """

    type: Optional[Any] = ["Category:OSWdac4a86a255853e6835f1f526ebc7d4b"]
    unit: Optional[SoundExposureUnit] = Field(
        SoundExposureUnit.pascal_squared_second, title="SoundExposureUnit"
    )



class ReactionRateConstantUnit(UnitEnum):
    meter_cubed_per_mole_per_second = "Item:OSW25bef56399fe5f7fa5d119aff09cfb30"
    centi_meter_cubed_per_mole_per_second = (
        "Item:OSW25bef56399fe5f7fa5d119aff09cfb30#OSWe3739db7a148562eb2f29ef963e3c001"
    )


class ReactionRateConstant(QuantityValue):
    """
    A quantity kind that is a proportionality constant that quantifies the relationship between the molar concentrations of the reactants and the rate of a second order chemical reaction.
    """

    type: Optional[Any] = ["Category:OSWec4a0bb9cee155e3a79994b906fbd3a7"]
    unit: Optional[ReactionRateConstantUnit] = Field(
        ReactionRateConstantUnit.meter_cubed_per_mole_per_second,
        title="ReactionRateConstantUnit",
    )



class RadianceUnit(UnitEnum):
    watt_per_meter_squared_per_steradian = "Item:OSW8afae973361b5e9ba300c36ac631da76"


class Radiance(QuantityValue):
    """
    "Radiance" is a radiometric measure that describes the amount of light that passes through or is emitted from a particular area, and falls within a given solid angle in a specified direction.
    """

    type: Optional[Any] = ["Category:OSWd50af2b5cb4c50b999266c4888e59657"]
    unit: Optional[RadianceUnit] = Field(
        RadianceUnit.watt_per_meter_squared_per_steradian, title="RadianceUnit"
    )



class PowerPerAreaUnit(UnitEnum):
    watt_per_meter_squared = "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11"
    watt_per_centi_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWa735be7b016c510f98dd404ee42c6722"
    )
    micro_watt_per_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWbec47ab085945564b8bc080ab7934395"
    )
    milli_watt_per_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWf33a1a99c6055b178a0b973e57e1aacb"
    )
    pico_watt_per_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWf194c328c8ef587c823773008774afc8"
    )


class PowerPerArea(QuantityValue):
    """
    This is an autogenerated partial class definition of 'PowerPerArea'
    """

    type: Optional[Any] = ["Category:OSW40c46aba16f45962a7330b7f8b88681e"]
    unit: Optional[PowerPerAreaUnit] = Field(
        PowerPerAreaUnit.watt_per_meter_squared, title="PowerPerAreaUnit"
    )



class MassEnergyTransferCoefficientUnit(UnitEnum):
    meter_squared_per_kilo_gram = (
        "Item:OSWd7015166d39d5cae866a40eac3d51896#OSWc811db362efa5d33a49b56ffdd77e54d"
    )


class MassEnergyTransferCoefficient(QuantityValue):
    """
    "Mass Energy Transfer Coefficient" is that fraction of the mass attenuation coefficient which contributes to the production of kinetic energy in charged particles.
    """

    type: Optional[Any] = ["Category:OSW62d08281552e55adacdc5be6123ac375"]
    unit: Optional[MassEnergyTransferCoefficientUnit] = Field(
        MassEnergyTransferCoefficientUnit.meter_squared_per_kilo_gram,
        title="MassEnergyTransferCoefficientUnit",
    )



class InverseTemperatureUnit(UnitEnum):
    per_kelvin = "Item:OSW33dfda3d4dea57d192d02eecdbc09b86"


class InverseTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseTemperature'
    """

    type: Optional[Any] = ["Category:OSW06018a46bc2e5b34bab4cc7e8d71bf87"]
    unit: Optional[InverseTemperatureUnit] = Field(
        InverseTemperatureUnit.per_kelvin, title="InverseTemperatureUnit"
    )



class PowerUnit(UnitEnum):
    watt = "Item:OSW58b03da1b2d35d8ca09043abb7fc8870"
    mega_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSWe5ebcb7476e154cba0bc729b319cafe9"
    )
    kilo_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSWea7d8a111eca57499c3fb187d61d3170"
    )
    pico_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSWff05f4ecc2a4513292fae2aa83798da1"
    )
    milli_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSW89c2f08b4360565cb2bfe50f5614a0d4"
    )
    nano_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSW3320aea347d45d0ebed5f48f7a5bf787"
    )
    tera_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSW4303ebb8138953509f12c795a591600c"
    )
    giga_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSW3cfa1cd0ef6651c3bad40ca56ea6878c"
    )
    micro_watt = (
        "Item:OSW58b03da1b2d35d8ca09043abb7fc8870#OSW5884b063f20a5ee19bef9444d5e10da9"
    )


class Power(QuantityValue):
    """
    Power is the rate at which work is performed or energy is transmitted, or the amount of energy required or expended for a given unit of time. As a rate of change of work done or the energy of a subsystem, power is: $P = W/t$, where $P$ is power, $W$ is work and {t} is time.
    """

    type: Optional[Any] = ["Category:OSWa819b53101b854ad923f9f13dfb41794"]
    unit: Optional[PowerUnit] = Field(PowerUnit.watt, title="PowerUnit")



class CatalyticActivityConcentrationUnit(UnitEnum):
    mole_per_meter_cubed_per_second = "Item:OSW030b700cf26d53fe804f2dcd9cbc44ca"


class CatalyticActivityConcentration(QuantityValue):
    """
    The catalytic activity of an enzyme per unit volume, where volume refers to that of the original enzyme‐containing preparation, not that of the assay system. It may be expressed in katals per litre.
    """

    type: Optional[Any] = ["Category:OSW6d3afdeb72075dae90dbb01171c2d1db"]
    unit: Optional[CatalyticActivityConcentrationUnit] = Field(
        CatalyticActivityConcentrationUnit.mole_per_meter_cubed_per_second,
        title="CatalyticActivityConcentrationUnit",
    )



class AngularMomentumUnit(UnitEnum):
    joule_second = "Item:OSWf045a04750e15ea2b152fb3bfebf162a"
    atto_joule_second = (
        "Item:OSWf045a04750e15ea2b152fb3bfebf162a#OSW3eaa66dd20f856fe9a5c4199bc0a1ea4"
    )


class AngularMomentum(QuantityValue):
    """
    Angular Momentum of an object rotating about some reference point is the measure of the extent to which the object will continue to rotate about that point unless acted upon by an external torque. In particular, if a point mass rotates about an axis, then the angular momentum with respect to a point on the axis is related to the mass of the object, the velocity and the distance of the mass to the axis. While the motion associated with linear momentum has no absolute frame of reference, the rotation associated with angular momentum is sometimes spoken of as being measured relative to the fixed stars.  $\textit{Angular Momentum}$, $\textit{Moment of Momentum}, or $\textit{Rotational Momentum", is a vector quantity that represents the product of a body's rotational inertia and rotational velocity about a particular axis.
    """

    type: Optional[Any] = ["Category:OSW11c230fdfd065eee822d39afdc9fba80"]
    unit: Optional[AngularMomentumUnit] = Field(
        AngularMomentumUnit.joule_second, title="AngularMomentumUnit"
    )



class AngularMomentumPerAngleUnit(UnitEnum):
    meter_newton_second_per_radian = "Item:OSW404a6456c6e85787a64ba84779ef3d70"


class AngularMomentumPerAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'AngularMomentumPerAngle'
    """

    type: Optional[Any] = ["Category:OSW313d97b5a2685dd6866686c37b62a259"]
    unit: Optional[AngularMomentumPerAngleUnit] = Field(
        AngularMomentumPerAngleUnit.meter_newton_second_per_radian,
        title="AngularMomentumPerAngleUnit",
    )



class EnergyFluenceUnit(UnitEnum):
    joule_per_meter_squared = "Item:OSW0747b5382b955ef2adef0e4c4b1efa81"
    mega_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSWf9cdbd6556545d55a9bde1a0915a9545"
    )
    milli_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW3b9b7dca35ec5f7995ba76de650fcadf"
    )
    joule_per_centi_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW16b24f4ffe12585aa114fbefbf3dbd5b"
    )
    giga_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW48c62f71ae5a512ca24dcb6059999b8d"
    )


class EnergyFluence(QuantityValue):
    """
    "Energy Fluence" can be used to describe the energy delivered per unit area
    """

    type: Optional[Any] = ["Category:OSWf182572936955b6e9f54d4d9bb89daf1"]
    unit: Optional[EnergyFluenceUnit] = Field(
        EnergyFluenceUnit.joule_per_meter_squared, title="EnergyFluenceUnit"
    )



class ConcentrationUnit(UnitEnum):
    mole_per_meter_cubed = "Item:OSW8ac2d9421f455305abb01a51d001cc54"
    pico_mole_per_meter_cubed = (
        "Item:OSW8ac2d9421f455305abb01a51d001cc54#OSW8bb63381b7c355e3984be7dca4baf030"
    )
    kilo_mole_per_meter_cubed = (
        "Item:OSW8ac2d9421f455305abb01a51d001cc54#OSWe718f1e8ec1952069a956ab1096f08cb"
    )
    milli_mole_per_meter_cubed = (
        "Item:OSW8ac2d9421f455305abb01a51d001cc54#OSWdc37f32c45c75ead9b0ac9a0547030eb"
    )
    mole_per_deci_meter_cubed = (
        "Item:OSW8ac2d9421f455305abb01a51d001cc54#OSW2c20bbad810959ffa4d1ea210b290227"
    )


class Concentration(QuantityValue):
    """
    In chemistry, concentration is defined as the abundance of a constituent divided by the total volume of a mixture. Furthermore, in chemistry, four types of mathematical description can be distinguished: mass concentration, molar concentration, number concentration, and volume concentration. The term concentration can be applied to any kind of chemical mixture, but most frequently it refers to solutes in solutions.
    """

    type: Optional[Any] = ["Category:OSW4ce5add385d2545ab8ab50e4b222dab4"]
    unit: Optional[ConcentrationUnit] = Field(
        ConcentrationUnit.mole_per_meter_cubed, title="ConcentrationUnit"
    )



class IonConcentrationUnit(UnitEnum):
    candela_per_lumen = "Item:OSWb175d26e736c5603bcaa1060f2afddff"
    candela_per_kilo_lumen = (
        "Item:OSWb175d26e736c5603bcaa1060f2afddff#OSW77b2c8bd92a057b1ade0ce1687eb7520"
    )


class IonConcentration(QuantityValue):
    """
    "Luminous Intensity Distribution" is a measure of the luminous intensity of a light source that changes according to the direction of the ray. It is normally based on some standardized distribution light distribution curves. Usually measured in Candela/Lumen (cd/lm) or (cd/klm).
    """

    type: Optional[Any] = ["Category:OSW9882e31701b25fa18ff69a38f57debf5"]
    unit: Optional[IonConcentrationUnit] = Field(
        IonConcentrationUnit.candela_per_lumen, title="IonConcentrationUnit"
    )



class AngularVelocityUnit(UnitEnum):
    radian_per_second = "Item:OSWb0010d0f4c7a52e18edbfdc34e4c0653"


class AngularVelocity(QuantityValue):
    """
    The change of angle per unit time; specifically, in celestial mechanics, the change in angle of the radius vector per unit time.
    """

    type: Optional[Any] = ["Category:OSWd76028b659105d139a01faedd83fefbd"]
    unit: Optional[AngularVelocityUnit] = Field(
        AngularVelocityUnit.radian_per_second, title="AngularVelocityUnit"
    )



class ElectricCurrentPerEnergyUnit(UnitEnum):
    ampere_per_joule = "Item:OSW35db123ef0b25089bab3d9eaa2b5cb67"


class ElectricCurrentPerEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ElectricCurrentPerEnergy'
    """

    type: Optional[Any] = ["Category:OSW898394101b5d59868314ca9df841107b"]
    unit: Optional[ElectricCurrentPerEnergyUnit] = Field(
        ElectricCurrentPerEnergyUnit.ampere_per_joule,
        title="ElectricCurrentPerEnergyUnit",
    )



class ElectricCurrentUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class ElectricCurrent(QuantityValue):
    """
    "Electric Current" is the flow (movement) of electric charge. The amount of electric current through some surface, for example, a section through a copper conductor, is defined as the amount of electric charge flowing through that surface over time. Current is a scalar-valued quantity. Electric current is one of the base quantities in the International System of Quantities, ISQ, on which the International System of Units, SI, is based.
    """

    type: Optional[Any] = ["Category:OSW7c210ed3aad85519ae7330073a9d6f9f"]
    unit: Optional[ElectricCurrentUnit] = Field(
        ElectricCurrentUnit.ampere, title="ElectricCurrentUnit"
    )



class DynamicViscosityUnit(UnitEnum):
    pascal_second = "Item:OSWfb230f7ff1a55c23accf8ae94aacc9e1"
    milli_pascal_second = (
        "Item:OSWfb230f7ff1a55c23accf8ae94aacc9e1#OSW8e1783ac9f0b5fe3b404dcfbce8940cb"
    )


class DynamicViscosity(QuantityValue):
    """
    A measure of the molecular frictional resistance of a fluid as calculated using Newton's law.
    """

    type: Optional[Any] = ["Category:OSW7b9c678b7f2d5b84bdfa0bf72f6d9ff2"]
    unit: Optional[DynamicViscosityUnit] = Field(
        DynamicViscosityUnit.pascal_second, title="DynamicViscosityUnit"
    )



class DisplacementCurrentDensityUnit(UnitEnum):
    ampere_per_meter_squared = "Item:OSW2b1e97f1edd650c088abbe8896fe0333"
    mega_ampere_per_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWd0a4ce0cc105550b9bcbc416589a1b85"
    )
    kilo_ampere_per_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWa80d9ac2c0455902ab9531512c9b7667"
    )
    ampere_per_milli_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSW8d7d0b57aaba5f8a8f40e8bacc5cb2f6"
    )
    ampere_per_centi_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWec1a540d03745760af1d26077e9d762e"
    )


class DisplacementCurrentDensity(QuantityValue):
    """
    $\text{Displacement Current Density}$ is the time rate of change of the $\textit{Electric Flux Density}$.
      This is a measure of how quickly the electric field changes if we observe it as a function of time.
      This is different than if we look at how the electric field changes spatially, that is, over a region of space for a fixed amount of time.
    """

    type: Optional[Any] = ["Category:OSW4838a6964ad458f685852d1a1a5a62ac"]
    unit: Optional[DisplacementCurrentDensityUnit] = Field(
        DisplacementCurrentDensityUnit.ampere_per_meter_squared,
        title="DisplacementCurrentDensityUnit",
    )



class SpecificHeatCapacityAtConstantPressureUnit(UnitEnum):
    joule_per_Celsius_per_kilo_gram = (
        "Item:OSW93d8b6e516fd54f09d483dee1278e3a8#OSWa0cd208ccfa759388597f5f9ff5c69fc"
    )


class SpecificHeatCapacityAtConstantPressure(QuantityValue):
    """
    Specific heat at a constant pressure.
    """

    type: Optional[Any] = ["Category:OSW12b88b32ed2f58c5aa633841b687b985"]
    unit: Optional[SpecificHeatCapacityAtConstantPressureUnit] = Field(
        SpecificHeatCapacityAtConstantPressureUnit.joule_per_Celsius_per_kilo_gram,
        title="SpecificHeatCapacityAtConstantPressureUnit",
    )



class ElectricFieldStrengthUnit(UnitEnum):
    volt_per_meter = "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb"
    micro_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSWe9e5b5d155c95fc9b3bc6f1ef6a63fa0"
    )
    volt_per_milli_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSW5503cb893f635d3a955c6be99f588596"
    )
    volt_per_centi_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSW68aa46316f8b5bfc83102870e2c9c5b4"
    )
    kilo_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSW9315a6f234fa567497c5344f4360ac89"
    )
    mega_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSWac4536de9cb25c1db8f0eb9f66e3fa25"
    )
    milli_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSWed56aa34d47a55a5bb40bc28cd4b1533"
    )


class ElectricFieldStrength(QuantityValue):
    """
    $\textit{Electric Field Strength}$ is the magnitude and direction of an electric field, expressed by the value of $E$, also referred to as $\color{indigo} {\textit{electric field intensity}}$ or simply the electric field.
    """

    type: Optional[Any] = ["Category:OSWc66c35bcf6bd5b08a2e9763d78a082cb"]
    unit: Optional[ElectricFieldStrengthUnit] = Field(
        ElectricFieldStrengthUnit.volt_per_meter, title="ElectricFieldStrengthUnit"
    )



class RadiantEnergyDensityUnit(UnitEnum):
    joule_per_meter_cubed = "Item:OSW9ea4bf89c42b56728392f1c55639ac18"
    mega_joule_per_meter_cubed = (
        "Item:OSW9ea4bf89c42b56728392f1c55639ac18#OSW7044da5ba4b45554b3acc6c6f3fc3624"
    )


class RadiantEnergyDensity(QuantityValue):
    """
    "Radiant Energy Density", or radiant power, is the radiant energy per unit volume.
    """

    type: Optional[Any] = ["Category:OSW1769676ffcbf589194751d0e0bb05902"]
    unit: Optional[RadiantEnergyDensityUnit] = Field(
        RadiantEnergyDensityUnit.joule_per_meter_cubed, title="RadiantEnergyDensityUnit"
    )



class EnergyDensityUnit(UnitEnum):
    joule_per_meter_cubed = "Item:OSW9ea4bf89c42b56728392f1c55639ac18"
    mega_joule_per_meter_cubed = (
        "Item:OSW9ea4bf89c42b56728392f1c55639ac18#OSW7044da5ba4b45554b3acc6c6f3fc3624"
    )


class EnergyDensity(QuantityValue):
    """
    Energy density is defined as energy per unit volume. The SI unit for energy density is the joule per cubic meter.
    """

    type: Optional[Any] = ["Category:OSWa7079f30224250c9b5d10367541f3c54"]
    unit: Optional[EnergyDensityUnit] = Field(
        EnergyDensityUnit.joule_per_meter_cubed, title="EnergyDensityUnit"
    )



class MassPerEnergyUnit(UnitEnum):
    kilo_gram_per_joule = "Item:OSW0ab2af45d05c527d8fe20509629f9ae3"


class MassPerEnergy(QuantityValue):
    """
    Mass per Energy is a physical quantity that can be used to relate the energy of a system to its mass.
    """

    type: Optional[Any] = ["Category:OSWdbee78c71c255e02babd2e594e503815"]
    unit: Optional[MassPerEnergyUnit] = Field(
        MassPerEnergyUnit.kilo_gram_per_joule, title="MassPerEnergyUnit"
    )



class ThermalInsulanceUnit(UnitEnum):
    kelvin_meter_squared_per_watt = "Item:OSWeb19f8b7b92a5f09a0a4a398d29021dc"


class ThermalInsulance(QuantityValue):
    """
    $\textit{Thermal Insulance}$ is the reduction of heat transfer (the transfer of thermal energy between objects of differing temperature) between objects in thermal contact or in range of radiative influence. In building technology, this quantity is often called $\textit{Thermal Resistance}$, with the symbol $R$.
    """

    type: Optional[Any] = ["Category:OSW8139b63734d3516c827b33f08ced96fb"]
    unit: Optional[ThermalInsulanceUnit] = Field(
        ThermalInsulanceUnit.kelvin_meter_squared_per_watt, title="ThermalInsulanceUnit"
    )



class ElectricFieldUnit(UnitEnum):
    volt_per_meter = "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb"
    micro_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSWe9e5b5d155c95fc9b3bc6f1ef6a63fa0"
    )
    volt_per_milli_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSW5503cb893f635d3a955c6be99f588596"
    )
    volt_per_centi_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSW68aa46316f8b5bfc83102870e2c9c5b4"
    )
    kilo_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSW9315a6f234fa567497c5344f4360ac89"
    )
    mega_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSWac4536de9cb25c1db8f0eb9f66e3fa25"
    )
    milli_volt_per_meter = (
        "Item:OSWd855ce693a6d5d3d8bdf5846093ae4fb#OSWed56aa34d47a55a5bb40bc28cd4b1533"
    )


class ElectricField(QuantityValue):
    """
    The space surrounding an electric charge or in the presence of a time-varying magnetic field has a property called an electric field. This electric field exerts a force on other electrically charged objects. In the idealized case, the force exerted between two point charges is inversely proportional to the square of the distance between them. (Coulomb's Law).
    """

    type: Optional[Any] = ["Category:OSW4f0b3f4a40ad5ffbb492a000abe2b30d"]
    unit: Optional[ElectricFieldUnit] = Field(
        ElectricFieldUnit.volt_per_meter, title="ElectricFieldUnit"
    )



class MassFlowRateUnit(UnitEnum):
    kilo_gram_per_second = (
        "Item:OSWf6bfa826fcea5795b76c5756f7ec78fb#OSWfe7b5227d12757e789055c9fd32d15e4"
    )


class MassFlowRate(QuantityValue):
    """
    "Mass Flow Rate" is a measure of Mass flux. The common symbol is $\dot{m}$ (pronounced $m-dot$), although sometimes $\mu$ is used. The SI units are $kg s-1$.
    """

    type: Optional[Any] = ["Category:OSW4a0860ff03e65af19b7c64e3b837fc81"]
    unit: Optional[MassFlowRateUnit] = Field(
        MassFlowRateUnit.kilo_gram_per_second, title="MassFlowRateUnit"
    )



class EnergyPerAreaUnit(UnitEnum):
    joule_per_meter_squared = "Item:OSW0747b5382b955ef2adef0e4c4b1efa81"
    mega_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSWf9cdbd6556545d55a9bde1a0915a9545"
    )
    milli_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW3b9b7dca35ec5f7995ba76de650fcadf"
    )
    joule_per_centi_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW16b24f4ffe12585aa114fbefbf3dbd5b"
    )
    giga_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW48c62f71ae5a512ca24dcb6059999b8d"
    )


class EnergyPerArea(QuantityValue):
    """
    Energy per unit area is a measure of the energy either impinging upon or generated from a given unit of area. This can be a measure of the "toughness" of a material, being the amount of energy that needs to be applied per unit area of a crack to cause it to fracture. This is a constant for a given material..
    """

    type: Optional[Any] = ["Category:OSW46d8ae433dda5e368d8e76800d85ee12"]
    unit: Optional[EnergyPerAreaUnit] = Field(
        EnergyPerAreaUnit.joule_per_meter_squared, title="EnergyPerAreaUnit"
    )



class PeriodUnit(UnitEnum):
    second = "Item:OSW85302b21cf045998b80f38c9fdb88f84"
    deci_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW78488a0c8e885365beff30aae10a4efd"
    )
    micro_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW90ff22cff2dd5d8ba6de84bf9a70c50c"
    )
    atto_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW2e4fec0373f45f1891403f06e433c5eb"
    )
    pico_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWc6f2918cbdef5bde8d00cf86938c7f8e"
    )
    milli_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW84d4f530814e5251b06e73ee0184e32b"
    )
    femto_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWd1e24421c83d5defb5c22e9a5fe490fb"
    )
    nano_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSW14e2efd7a4a05306a74663592edb23e8"
    )
    kilo_second = (
        "Item:OSW85302b21cf045998b80f38c9fdb88f84#OSWbc38445f00d056069fef04f8e25c66f6"
    )


class Period(QuantityValue):
    """
    Duration of one cycle of a periodic phenomenon.
    """

    type: Optional[Any] = ["Category:OSW651ad86866765ae79d2702fffa50f4d8"]
    unit: Optional[PeriodUnit] = Field(PeriodUnit.second, title="PeriodUnit")



class MomentOfInertiaUnit(UnitEnum):
    kilo_gram_meter_squared = "Item:OSWd211fc61709b5e48a4c96473c86a8d13"


class MomentOfInertia(QuantityValue):
    """
    The rotational inertia or resistance to change in direction or speed of rotation about a defined axis.
    """

    type: Optional[Any] = ["Category:OSW2e958a0e653558a8abf2bd1fa3c6dd59"]
    unit: Optional[MomentOfInertiaUnit] = Field(
        MomentOfInertiaUnit.kilo_gram_meter_squared, title="MomentOfInertiaUnit"
    )



class ElectricDipoleMomentUnit(UnitEnum):
    coulomb_meter = "Item:OSW1daae0d7c4d35d3e8a523ce4f9c64970"


class ElectricDipoleMoment(QuantityValue):
    """
    "Electric Dipole Moment" is a measure of the separation of positive and negative electrical charges in a system of (discrete or continuous) charges. It is a vector-valued quantity. If the system of charges is neutral, that is if the sum of all charges is zero, then the dipole moment of the system is independent of the choice of a reference frame; however in a non-neutral system, such as the dipole moment of a single proton, a dependence on the choice of reference point arises. In such cases it is conventional to choose the reference point to be the center of mass of the system or the center of charge, not some arbitrary origin. This convention ensures that the dipole moment is an intrinsic property of the system. The electric dipole moment of a substance within a domain is the vector sum of electric dipole moments of all electric dipoles included in the domain.
    """

    type: Optional[Any] = ["Category:OSWe21f6c5e4c5e5b5b9f86920aec0eaae7"]
    unit: Optional[ElectricDipoleMomentUnit] = Field(
        ElectricDipoleMomentUnit.coulomb_meter, title="ElectricDipoleMomentUnit"
    )



class PressureInRelationToVolumeFlowRateUnit(UnitEnum):
    pascal_second_per_meter_cubed = "Item:OSW975f79935c9f543caaec4538d778a2f5"


class PressureInRelationToVolumeFlowRate(QuantityValue):
    """
    This is an autogenerated partial class definition of 'PressureInRelationToVolumeFlowRate'
    """

    type: Optional[Any] = ["Category:OSWb56d701632ee5ee3afe3ef624ae41753"]
    unit: Optional[PressureInRelationToVolumeFlowRateUnit] = Field(
        PressureInRelationToVolumeFlowRateUnit.pascal_second_per_meter_cubed,
        title="PressureInRelationToVolumeFlowRateUnit",
    )



class RadiantFluenceUnit(UnitEnum):
    joule_per_meter_squared = "Item:OSW0747b5382b955ef2adef0e4c4b1efa81"
    mega_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSWf9cdbd6556545d55a9bde1a0915a9545"
    )
    milli_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW3b9b7dca35ec5f7995ba76de650fcadf"
    )
    joule_per_centi_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW16b24f4ffe12585aa114fbefbf3dbd5b"
    )
    giga_joule_per_meter_squared = (
        "Item:OSW0747b5382b955ef2adef0e4c4b1efa81#OSW48c62f71ae5a512ca24dcb6059999b8d"
    )


class RadiantFluence(QuantityValue):
    """
    Radiant fluence rate, or spherical irradiance, is equal to the total radiant flux incident on a small sphere divided by the area of the diametrical cross-section of the sphere.
    """

    type: Optional[Any] = ["Category:OSW94e4c35a2f775b81bdf2cd9d259082ba"]
    unit: Optional[RadiantFluenceUnit] = Field(
        RadiantFluenceUnit.joule_per_meter_squared, title="RadiantFluenceUnit"
    )



class IonicStrengthUnit(UnitEnum):
    mole_per_kilo_gram = "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b"
    centi_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW9abfd6b6d96b507abac8057d6e35a74f"
    )
    micro_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSWa9d227b6d12958eba67fdf22b0934535"
    )
    femto_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSWce6b64163d095affbef6daa39c9cd063"
    )
    pico_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSWd77b5543087f560caec2016c89521715"
    )
    milli_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW78a5da75d0d15046935df4e27fa7d3a9"
    )
    nano_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW51bd13e67a4758bba50388bd5cffe504"
    )
    kilo_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW84e7943cec52598082a96c43ab77d33a"
    )


class IonicStrength(QuantityValue):
    """
    The "Ionic Strength" of a solution is a measure of the concentration of ions in that solution.
    """

    type: Optional[Any] = ["Category:OSWb691a525fb3f5892a203e1246382b04b"]
    unit: Optional[IonicStrengthUnit] = Field(
        IonicStrengthUnit.mole_per_kilo_gram, title="IonicStrengthUnit"
    )



class AngularFrequencyUnit(UnitEnum):
    radian_per_second = "Item:OSWb0010d0f4c7a52e18edbfdc34e4c0653"


class AngularFrequency(QuantityValue):
    """
    "Angular frequency", symbol $\omega$ (also referred to by the terms angular speed, radial frequency, circular frequency, orbital frequency, radian frequency, and pulsatance) is a scalar measure of rotation rate. Angular frequency (or angular speed) is the magnitude of the vector quantity angular velocity.
    """

    type: Optional[Any] = ["Category:OSW9534c898b7d45510adfa6673507a4e10"]
    unit: Optional[AngularFrequencyUnit] = Field(
        AngularFrequencyUnit.radian_per_second, title="AngularFrequencyUnit"
    )



class SoundExposureLevelUnit(UnitEnum):
    byte = "Item:OSW20ac6724f1a05ee884222d546955e78f"


class SoundExposureLevel(QuantityValue):
    """
    Sound Exposure Level abbreviated as $SEL$ and $LAE$, is the total noise energy produced from a single noise event, expressed as a logarithmic ratio from a reference level.
    """

    type: Optional[Any] = ["Category:OSW4e21f4a2c9065a73aebb426c037f5362"]
    unit: Optional[SoundExposureLevelUnit] = Field(
        SoundExposureLevelUnit.byte, title="SoundExposureLevelUnit"
    )



class TotalCurrentUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class TotalCurrent(QuantityValue):
    """
    "Total Current" is the sum of the electric current that is flowing through a surface and the displacement current.
    """

    type: Optional[Any] = ["Category:OSW527cea47c2575449a1a4f61349f12ee5"]
    unit: Optional[TotalCurrentUnit] = Field(
        TotalCurrentUnit.ampere, title="TotalCurrentUnit"
    )



class SpecificPowerUnit(UnitEnum):
    gray_per_second = "Item:OSW4cbc32faa6945fea85c32ee675aff008"


class SpecificPower(QuantityValue):
    """
    Specific power, also known as power-to-weight ratio, is the amount of power output per unit mass of the power source. It is generally used to measure the performance of that power source. The higher the ratio, the more power a system produces relative to its weight. It's commonly used in the automotive and aerospace industries to compare the performance of different engines. It's generally measured in watts per kilogram (W/kg) or horsepower per pound (hp/lb).
    """

    type: Optional[Any] = ["Category:OSW592625bd38e75a4e87d866ef370b8a6c"]
    unit: Optional[SpecificPowerUnit] = Field(
        SpecificPowerUnit.gray_per_second, title="SpecificPowerUnit"
    )



class AcidityUnit(UnitEnum):
    pico_henry = "Item:OSW50e9172c55045cb3b1460b1345303ed2"


class Acidity(QuantityValue):
    """
    Chemicals or substances having a pH less than 7 are said to be acidic; lower pH means higher acidity.
    """

    type: Optional[Any] = ["Category:OSWd74bd57b722d57c0bd1316fb700b8043"]
    unit: Optional[AcidityUnit] = Field(AcidityUnit.pico_henry, title="AcidityUnit")



class MassTemperatureUnit(UnitEnum):
    kelvin_kilo_gram = "Item:OSWfd24f9425d815d66beab746eecaf5926"


class MassTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'MassTemperature'
    """

    type: Optional[Any] = ["Category:OSW6847f51b03eb5ed6b4cda9e82af5e51a"]
    unit: Optional[MassTemperatureUnit] = Field(
        MassTemperatureUnit.kelvin_kilo_gram, title="MassTemperatureUnit"
    )



class MolarHeatCapacityUnit(UnitEnum):
    joule_per_kelvin_per_mole = "Item:OSW6d40ac4bdbc950ec9290f6a47ce23d20"


class MolarHeatCapacity(QuantityValue):
    """
    "Molar Heat Capacity" is the amount of heat energy required to raise the temperature of 1 mole of a substance. In SI units, molar heat capacity (symbol: cn) is the amount of heat in joules required to raise 1 mole of a substance 1 Kelvin.
    """

    type: Optional[Any] = ["Category:OSWd3bbec0b8c445d8a9b7aa98383fce1ad"]
    unit: Optional[MolarHeatCapacityUnit] = Field(
        MolarHeatCapacityUnit.joule_per_kelvin_per_mole, title="MolarHeatCapacityUnit"
    )



class MassPerAreaUnit(UnitEnum):
    kilo_gram_per_meter_squared = (
        "Item:OSWb93e608c86fd5480a5de9cd1b3e9ea22#OSW86b6ab5f70aa5624be17645333d53d51"
    )


class MassPerArea(QuantityValue):
    """
    The area density (also known as areal density, surface density, or superficial density) of a two-dimensional object is calculated as the mass per unit area. The SI derived unit is: kilogram per square metre  ($kg \cdot m^{-2}$).
    """

    type: Optional[Any] = ["Category:OSWb9612bfb909c5eab9e57e8d8a6c86082"]
    unit: Optional[MassPerAreaUnit] = Field(
        MassPerAreaUnit.kilo_gram_per_meter_squared, title="MassPerAreaUnit"
    )



class SpecificWeightUnit(UnitEnum):
    newton_per_meter_cubed = "Item:OSWf3f9733d84285a338b5b7306145c9b6d"
    kilo_newton_per_meter_cubed = (
        "Item:OSWf3f9733d84285a338b5b7306145c9b6d#OSWfe42a11de5995fa380fbde579c89484c"
    )


class SpecificWeight(QuantityValue):
    """
    The specific weight, also known as the unit weight is a volume-specific quantity defined as the weight per unit volume of a material. Note that weight is defined as a force, distinct from mass.
    """

    type: Optional[Any] = ["Category:OSW3b186dbd80f75c3a82cd7418d4d3ea53"]
    unit: Optional[SpecificWeightUnit] = Field(
        SpecificWeightUnit.newton_per_meter_cubed, title="SpecificWeightUnit"
    )



class PropagationCoefficientUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class PropagationCoefficient(QuantityValue):
    """
    The propagation constant, symbol $\gamma$, for a given system is defined by the ratio of the amplitude at the source of the wave to the amplitude at some distance x.
    """

    type: Optional[Any] = ["Category:OSWeee790c23e775ec2a852845b671532df"]
    unit: Optional[PropagationCoefficientUnit] = Field(
        PropagationCoefficientUnit.per_meter, title="PropagationCoefficientUnit"
    )



class ReluctanceUnit(UnitEnum):
    per_henry = "Item:OSW8a3b2c786aeb55f7a8a6be1fe96329a1"


class Reluctance(QuantityValue):
    """
    "Reluctance" or magnetic resistance, is a concept used in the analysis of magnetic circuits. It is analogous to resistance in an electrical circuit, but rather than dissipating electric energy it stores magnetic energy. In likeness to the way an electric field causes an electric current to follow the path of least resistance, a magnetic field causes magnetic flux to follow the path of least magnetic reluctance. It is a scalar, extensive quantity, akin to electrical resistance.
    """

    type: Optional[Any] = ["Category:OSW9eeda948d38a55948bfc8acd78bc8293"]
    unit: Optional[ReluctanceUnit] = Field(
        ReluctanceUnit.per_henry, title="ReluctanceUnit"
    )



class LengthEnergyUnit(UnitEnum):
    fermi_mega_electron_volt = "Item:OSW8a2c52d852d358a79e43fa4496c65528"


class LengthEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'LengthEnergy'
    """

    type: Optional[Any] = ["Category:OSWebfe11838eec5b17a7f242ea30869fbb"]
    unit: Optional[LengthEnergyUnit] = Field(
        LengthEnergyUnit.fermi_mega_electron_volt, title="LengthEnergyUnit"
    )



class RelativePressureCoefficientUnit(UnitEnum):
    per_kelvin = "Item:OSW33dfda3d4dea57d192d02eecdbc09b86"


class RelativePressureCoefficient(QuantityValue):
    """
    This is an autogenerated partial class definition of 'RelativePressureCoefficient'
    """

    type: Optional[Any] = ["Category:OSW7d5aaca50d5d5e798ac29a9e209310cf"]
    unit: Optional[RelativePressureCoefficientUnit] = Field(
        RelativePressureCoefficientUnit.per_kelvin,
        title="RelativePressureCoefficientUnit",
    )



class PowerAreaUnit(UnitEnum):
    meter_squared_watt = "Item:OSWcd571060b6f15f6288ef0ea01ad2c692"


class PowerArea(QuantityValue):
    """
    This is an autogenerated partial class definition of 'PowerArea'
    """

    type: Optional[Any] = ["Category:OSWce3eefbdaa425a1b90bd544840917d6a"]
    unit: Optional[PowerAreaUnit] = Field(
        PowerAreaUnit.meter_squared_watt, title="PowerAreaUnit"
    )



class IsentropicCompressibilityUnit(UnitEnum):
    per_pascal = "Item:OSWf030abd4441d52a7a8c5f84950985ea4"


class IsentropicCompressibility(QuantityValue):
    """
    Isentropic compressibility is the extent to which a material reduces its volume when it is subjected to compressive stresses at a constant value of entropy.
    """

    type: Optional[Any] = ["Category:OSWcb348455e271512e9dafd64590f71d78"]
    unit: Optional[IsentropicCompressibilityUnit] = Field(
        IsentropicCompressibilityUnit.per_pascal, title="IsentropicCompressibilityUnit"
    )



class LuminousFluxPerAreaUnit(UnitEnum):
    lux = "Item:OSWca14d08a41b65ac59d79d96be1351305"


class LuminousFluxPerArea(QuantityValue):
    """
    In photometry, illuminance is the total luminous flux incident on a surface, per unit area. It is a measure of how much the incident light illuminates the surface, wavelength-weighted by the luminosity function to correlate with human brightness perception. Similarly, luminous emittance is the luminous flux per unit area emitted from a surface. In SI derived units these are measured in $lux (lx)$ or $lumens per square metre$ ($cd \cdot m^{-2}$). In the CGS system, the unit of illuminance is the $phot$, which is equal to $10,000 lux$. The $foot-candle$ is a non-metric unit of illuminance that is used in photography.
    """

    type: Optional[Any] = ["Category:OSW79225fde5f8059d1802f8181c06b4cfa"]
    unit: Optional[LuminousFluxPerAreaUnit] = Field(
        LuminousFluxPerAreaUnit.lux, title="LuminousFluxPerAreaUnit"
    )



class InversePermittivityUnit(UnitEnum):
    meter_per_farad = "Item:OSW7897b70c933d560b918444de17703f23"


class InversePermittivity(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InversePermittivity'
    """

    type: Optional[Any] = ["Category:OSW4307744db9bb582aa546240504683af7"]
    unit: Optional[InversePermittivityUnit] = Field(
        InversePermittivityUnit.meter_per_farad, title="InversePermittivityUnit"
    )



class AmountOfSubstanceUnit(UnitEnum):
    mole = "Item:OSW4d9412cede875e399cffb35415646316"
    milli_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSW09461c4b2fa85ab683a3572a199ef16b"
    )
    kilo_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSW2971b3cb7eca516184282ecfa45bfb81"
    )
    femto_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSWb4b00897b51e505a8c8cac8d6958b73b"
    )
    micro_mole = (
        "Item:OSW4d9412cede875e399cffb35415646316#OSW1d4f11a4a1425dba81c9dac510278967"
    )


class AmountOfSubstance(QuantityValue):
    """
    $\textit{Amount of Substance}$ is a standards-defined quantity that measures the size of an ensemble of elementary entities,
       such as atoms, molecules, electrons, and other particles.
      It is sometimes referred to as chemical amount.

      The International System of Units (SI) defines the amount of substance to be proportional to the number of elementary entities present.
      The SI unit for amount of substance is mole.
      It has the unit symbol $mol$.

      The mole is defined as the amount of substance that contains an equal number of elementary entities as there are atoms in 0.012kg of the isotope carbon-12.
      This number is called Avogadro's number and has the value $6.02214179(30) \times 10^{23}$.

      The only other unit of amount of substance in current use is the $pound-mole$ with the symbol $lb-mol$,
       which is sometimes used in chemical engineering in the United States.
      One $pound-mole$ is exactly $453.59237 mol$.
    """

    type: Optional[Any] = ["Category:OSW2f222621d774517193dc5eab674e3721"]
    unit: Optional[AmountOfSubstanceUnit] = Field(
        AmountOfSubstanceUnit.mole, title="AmountOfSubstanceUnit"
    )



class MassConcentrationUnit(UnitEnum):
    gram_per_liter = "Item:OSW754b1a3564725113ac583f91ae2ea959"
    milli_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWca4043a385f25aa3a98122f2aefd0d2e"
    )
    micro_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW457d0485a44c57cda788a583bf9ab4ff"
    )
    gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWe905ceb23b3b550489bed5baa6c9b466"
    )
    kilo_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW40c933269ec45fc1aeef04aefce2b374"
    )
    pico_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW84ec459d4d135bf28a610cd00061d18c"
    )
    milli_gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW99bbcff947e1508bad38d748ad6ff8e2"
    )
    gram_per_deci_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW1a48aea5dca45c34bbde02b0df02f6f8"
    )
    femto_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW449dc7494f3f5c0bbd9aff1d1fd2f591"
    )
    nano_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW42fdef27c8ae5c8fbf1876c400f27101"
    )


class MassConcentration(QuantityValue):
    """
    The "Mass Concentration" of substance B  is defined as the mass of a constituent  divided by the volume of the mixture .
    """

    type: Optional[Any] = ["Category:OSW8276dacc03f051d9a4925398eff293b0"]
    unit: Optional[MassConcentrationUnit] = Field(
        MassConcentrationUnit.gram_per_liter, title="MassConcentrationUnit"
    )



class ParticleFluenceUnit(UnitEnum):
    per_meter_squared = "Item:OSW3adb44b7a27d5ed0b9691b095779cb1f"


class ParticleFluence(QuantityValue):
    """
    "Particle Fluence" is the total number of particles that intersect a unit area in a specific time interval of interest, and has units of /m2 (number of particles per meter squared).
    """

    type: Optional[Any] = ["Category:OSW0f5611df8241549893b5bd0a8e137680"]
    unit: Optional[ParticleFluenceUnit] = Field(
        ParticleFluenceUnit.per_meter_squared, title="ParticleFluenceUnit"
    )



class MolarVolumeUnit(UnitEnum):
    meter_cubed_per_mole = "Item:OSW94bba2ee2f9a573eb5fa99c9331f1626"
    deci_meter_cubed_per_mole = (
        "Item:OSW94bba2ee2f9a573eb5fa99c9331f1626#OSW6eaa02f1d5ad581f97e7e017fab31412"
    )
    centi_meter_cubed_per_mole = (
        "Item:OSW94bba2ee2f9a573eb5fa99c9331f1626#OSW90c99a00002b5483a1ac0638fdbe9078"
    )


class MolarVolume(QuantityValue):
    """
    The molar volume, symbol $V_m$, is the volume occupied by one mole of a substance (chemical element or chemical compound) at a given temperature and pressure. It is equal to the molar mass ($M$) divided by the mass density ($\rho$). It has the SI unit cubic metres per mole ($m^{1}/mol$). For ideal gases, the molar volume is given by the ideal gas equation: this is a good approximation for many common gases at standard temperature and pressure. For crystalline solids, the molar volume can be measured by X-ray crystallography.
    """

    type: Optional[Any] = ["Category:OSW80447c001b965c23a3d75ae4dc365fa8"]
    unit: Optional[MolarVolumeUnit] = Field(
        MolarVolumeUnit.meter_cubed_per_mole, title="MolarVolumeUnit"
    )



class ResistanceUnit(UnitEnum):
    ohm = "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1"
    kilo_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5e05beabf6935ae2b559c1cffc788110"
    )
    milli_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWa8d17cb3f4255320af6052cbd471d716"
    )
    tera_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5196e38637c752e58c2b5be5521e4234"
    )
    giga_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW66dbbd77c6ca5d5684b223fdfcc7b773"
    )
    mega_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW14b14dd3c32d5ee199a67e3796734a4a"
    )
    micro_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWacd4090bd8335717b6eea6b8c1151b29"
    )


class Resistance(QuantityValue):
    """
    The electrical resistance of an object is a measure of its opposition to the passage of a steady electric current.
    """

    type: Optional[Any] = ["Category:OSWb3794ddaf0f551c1bccb9b12a0190888"]
    unit: Optional[ResistanceUnit] = Field(ResistanceUnit.ohm, title="ResistanceUnit")



class BloodGlucoseLevelByMassUnit(UnitEnum):
    gram_per_liter = "Item:OSW754b1a3564725113ac583f91ae2ea959"
    milli_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWca4043a385f25aa3a98122f2aefd0d2e"
    )
    micro_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW457d0485a44c57cda788a583bf9ab4ff"
    )
    gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWe905ceb23b3b550489bed5baa6c9b466"
    )
    kilo_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW40c933269ec45fc1aeef04aefce2b374"
    )
    pico_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW84ec459d4d135bf28a610cd00061d18c"
    )
    milli_gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW99bbcff947e1508bad38d748ad6ff8e2"
    )
    gram_per_deci_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW1a48aea5dca45c34bbde02b0df02f6f8"
    )
    femto_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW449dc7494f3f5c0bbd9aff1d1fd2f591"
    )
    nano_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW42fdef27c8ae5c8fbf1876c400f27101"
    )


class BloodGlucoseLevelByMass(QuantityValue):
    """
    Blood sugar level, blood sugar concentration, or blood glucose level is the amount of glucose present in the blood of humans and animals.
      Glucose is a simple sugar and approximately 4 grams of glucose are present in the blood of humans at all times.
      Stored in skeletal muscle and liver cells in the form of glycogen, the body tightly regulates blood glucose levels as a part of metabolic homeostasis.
      During fasting blood glucose is maintained at a constant level at the expense of the glycogen stores in the liver and skeletal muscle.
      There are two main methods of describing concentrations: by weight, and by molecular count.
      Weights are in grams and molecular counts in moles.
      A mole is $6.022\times 10^{23}$ molecules.
      In both cases, the unit is usually modified by $milli-$ or $micro-$ or other prefix,
       and is always $per$ some volume, often a litre.
      Conversion factors depend on the molecular weight of the substance in question.
      $mmol/L$ is millimoles/liter, and is the world standard unit for measuring glucose in blood.
      Specifically, it is the designated SI (Systeme International) unit.
      Some countries use $mg/dl$.
      A mole is about $6\times 10^{23}$ molecules.
      $mg/dL$ (milligrams/deciliter) is the traditional unit for measuring $bG$ (blood glucose).
      There is a trend toward using $mmol/L$ however $mg/dL$ is much in practice.
      Some use is made of $mmol/L$ as the primary unit with $mg/dL$ quoted in parentheses.
      This acknowledges the large base of health care providers, researchers and patients who are already familiar with $mg/dL$.
    """

    type: Optional[Any] = ["Category:OSWad52711f3c225826942365d4930ff84c"]
    unit: Optional[BloodGlucoseLevelByMassUnit] = Field(
        BloodGlucoseLevelByMassUnit.gram_per_liter, title="BloodGlucoseLevelByMassUnit"
    )



class LinearAttenuationCoefficientUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class LinearAttenuationCoefficient(QuantityValue):
    """
    "Linear Attenuation Coefficient", also called the attenuation coefficient,  narrow beam attenuation coefficient, or absorption coefficient, is a quantity that characterizes how easily a material or medium can be penetrated by a beam of light, sound, particles, or other energy or matter.
    """

    type: Optional[Any] = ["Category:OSW15273de40c545109b5f30c7672e9b514"]
    unit: Optional[LinearAttenuationCoefficientUnit] = Field(
        LinearAttenuationCoefficientUnit.per_meter,
        title="LinearAttenuationCoefficientUnit",
    )



class VelocityUnit(UnitEnum):
    meter_per_second = "Item:OSW78331234e1a15aeebd8b0caa71201939"
    centi_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWd094e4cfd62c52248aad5ef87c19fb7d"
    )
    micro_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWfc9fca27ba5b543c8780521b4af39189"
    )
    milli_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW4937ac85021f506cb7ba3958f2216bd1"
    )
    kilo_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW9f12ce12bc725cd59791265e2e480fd2"
    )


class Velocity(QuantityValue):
    """
    In kinematics, velocity is the speed of an object and a specification of its direction of motion. Speed describes only how fast an object is moving, whereas velocity gives both how fast and in what direction the object is moving.
    """

    type: Optional[Any] = ["Category:OSW397c67ece63a5a5c96bad9349f49f3d7"]
    unit: Optional[VelocityUnit] = Field(
        VelocityUnit.meter_per_second, title="VelocityUnit"
    )



class LinearElectricCurrentDensityUnit(UnitEnum):
    ampere_per_meter = "Item:OSW21e01a5082e35d5cbcf741df0a054cee"
    ampere_per_milli_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSW81d243ef653b5b6b890b1102d37d6d78"
    )
    milli_ampere_per_milli_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSWe385b197cb0e581d8e25ce1ec9a73c7a"
    )
    kilo_ampere_per_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSWe299bb79004b52b3a4c9f8a739b881bf"
    )
    ampere_per_centi_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSW8d315234960451fa895c98b88e9f1b28"
    )


class LinearElectricCurrentDensity(QuantityValue):
    """
    "Linear Electric Linear Current Density" is the electric current per unit length. Electric current, $I$, through a curve $C$ is defined as $I = \int_C J _s \times e_n$, where $e_n$ is a unit vector perpendicular to the surface and line vector element, and $dr$ is the differential of position vector $r$.
    """

    type: Optional[Any] = ["Category:OSW6ce762ef103d5b15976dcfa13914bef4"]
    unit: Optional[LinearElectricCurrentDensityUnit] = Field(
        LinearElectricCurrentDensityUnit.ampere_per_meter,
        title="LinearElectricCurrentDensityUnit",
    )



class MomentumPerAngleUnit(UnitEnum):
    newton_second_per_radian = "Item:OSW7f98af11c42058aeb941076309b78dea"


class MomentumPerAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'MomentumPerAngle'
    """

    type: Optional[Any] = ["Category:OSW9ecfc2e097565a469701e0a2c23e57fb"]
    unit: Optional[MomentumPerAngleUnit] = Field(
        MomentumPerAngleUnit.newton_second_per_radian, title="MomentumPerAngleUnit"
    )



class ForcePerElectricChargeUnit(UnitEnum):
    newton_per_coulomb = "Item:OSW3ce8ee5544995c36be4ab4d2f34e037e"


class ForcePerElectricCharge(QuantityValue):
    """
    The electric field depicts the force exerted on other electrically charged objects by the electrically charged particle the field is surrounding. The electric field is a vector field with SI units of newtons per coulomb ($N C^{-1}$) or, equivalently, volts per metre ($V m^{-1}$ ). The SI base units of the electric field are $kg m s^{-3} A^{-1}$. The strength or magnitude of the field at a given point is defined as the force that would be exerted on a positive test charge of 1 coulomb placed at that point
    """

    type: Optional[Any] = ["Category:OSW3db28177ab145fceab8085ac3b0c94d2"]
    unit: Optional[ForcePerElectricChargeUnit] = Field(
        ForcePerElectricChargeUnit.newton_per_coulomb,
        title="ForcePerElectricChargeUnit",
    )



class AreaPerTimeUnit(UnitEnum):
    meter_squared_per_second = "Item:OSW20b837bfd2fa5c3abc86347ce702f27c"
    milli_meter_squared_per_second = (
        "Item:OSW20b837bfd2fa5c3abc86347ce702f27c#OSW5db8f161eb8c59129cef62d84dd3309c"
    )
    centi_meter_squared_per_second = (
        "Item:OSW20b837bfd2fa5c3abc86347ce702f27c#OSW031bb99ee99a5794a24c66e6203c21db"
    )


class AreaPerTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'AreaPerTime'
    """

    type: Optional[Any] = ["Category:OSW64892b4f11e852b1873975a66e851abe"]
    unit: Optional[AreaPerTimeUnit] = Field(
        AreaPerTimeUnit.meter_squared_per_second, title="AreaPerTimeUnit"
    )



class ThermalResistanceUnit(UnitEnum):
    kelvin_per_watt = "Item:OSW3e3198453a27527ead13a1e41cd9d0f0"


class ThermalResistance(QuantityValue):
    """
    $\textit{Thermal Resistance}$ is a heat property and a measure of a temperature difference by which an object or material resists a heat flow (heat per time unit or thermal resistance). Thermal resistance is the reciprocal thermal conductance. the thermodynamic temperature difference divided by heat flow rate. Thermal resistance $R$ has the units $\frac{m^2 \cdot K}{W}$.
    """

    type: Optional[Any] = ["Category:OSW55e45a78a82854228a5ac2e6893d1d95"]
    unit: Optional[ThermalResistanceUnit] = Field(
        ThermalResistanceUnit.kelvin_per_watt, title="ThermalResistanceUnit"
    )



class NEON(QuantityValue):
    """
    Variance for NEON conductivity data measured in MicroS-PER-CM
    """

    type: Optional[Any] = ["Category:OSW2bd655adef375aa0a5e4c1192efbb2e6"]
    unit: Optional[NEONUnit] = Field(
        NEONUnit.Celsius_squared, title="NEONUnit"
    )



class AngularCrossSectionUnit(UnitEnum):
    meter_squared_per_steradian = "Item:OSWe9c4745c4d3a5c17a288b08a7f870ffc"


class AngularCrossSection(QuantityValue):
    """
    "Angular Cross-section" is the cross-section for ejecting or scattering a particle into an elementary cone, divided by the solid angle $d\Omega$ of that cone.
    """

    type: Optional[Any] = ["Category:OSWa1a449c3adf35ee3aba8109c7667b890"]
    unit: Optional[AngularCrossSectionUnit] = Field(
        AngularCrossSectionUnit.meter_squared_per_steradian,
        title="AngularCrossSectionUnit",
    )



class MagneticFluxDensityUnit(UnitEnum):
    tesla = "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0"
    micro_tesla = (
        "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0#OSW30a0158af5445fbc8b08c843d0a84d5a"
    )
    milli_tesla = (
        "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0#OSW490afd74306a568c858e46dd393110fe"
    )
    nano_tesla = (
        "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0#OSW7b67d49640c75e54b4906f4bd72b494b"
    )


class MagneticFluxDensity(QuantityValue):
    """
    "Magnetic Flux Density" is a vector quantity and is the magnetic flux per unit area of a magnetic field at right angles to the magnetic force. It can be defined in terms of the effects the field has, for example by $B = F/q v \sin \theta$, where $F$ is the force a moving charge $q$ would experience if it was travelling at a velocity $v$ in a direction making an angle θ with that of the field. The magnetic field strength is also a vector quantity and is related to $B$ by: $H = B/\mu$, where $\mu$ is the permeability of the medium.
    """

    type: Optional[Any] = ["Category:OSW91fc2f110c7f52628dce39bc0278562b"]
    unit: Optional[MagneticFluxDensityUnit] = Field(
        MagneticFluxDensityUnit.tesla, title="MagneticFluxDensityUnit"
    )



class TemperaturePerMagneticFluxDensityUnit(UnitEnum):
    kelvin_per_tesla = "Item:OSW5b9ccf8109b457aca03dbd2a487500ed"


class TemperaturePerMagneticFluxDensity(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TemperaturePerMagneticFluxDensity'
    """

    type: Optional[Any] = ["Category:OSW844bb46fae8752d2b8e7f59939d7e47d"]
    unit: Optional[TemperaturePerMagneticFluxDensityUnit] = Field(
        TemperaturePerMagneticFluxDensityUnit.kelvin_per_tesla,
        title="TemperaturePerMagneticFluxDensityUnit",
    )



class WarpingConstantUnit(UnitEnum):
    field_6 = "Item:OSWc5904c8a783d5e8da5f6a24745774a6b"
    field_6_1 = (
        "Item:OSWc5904c8a783d5e8da5f6a24745774a6b#OSWffc057592b945f8aaad8ef5e3e1903a4"
    )


class WarpingConstant(QuantityValue):
    """
    The "Warping Constant" is a measure for the warping constant or warping resistance of a cross section under torsional loading. It is usually measured in m⁶.
    """

    type: Optional[Any] = ["Category:OSW298b2f8a4a0155aa951ae75231e4343f"]
    unit: Optional[WarpingConstantUnit] = Field(
        WarpingConstantUnit.field_6, title="WarpingConstantUnit"
    )



class ForceUnit(UnitEnum):
    newton = "Item:OSW8113ac9c25615c21902a9447ab03cc0a"
    milli_newton = (
        "Item:OSW8113ac9c25615c21902a9447ab03cc0a#OSWf2fd2b42f5a653f398f9fb35200f39fe"
    )
    micro_newton = (
        "Item:OSW8113ac9c25615c21902a9447ab03cc0a#OSW31a9dadf838358bfa5504d7781711397"
    )
    kilo_newton = (
        "Item:OSW8113ac9c25615c21902a9447ab03cc0a#OSW9e26f43774ed54c9b9bf757fca6ad5e7"
    )
    mega_newton = (
        "Item:OSW8113ac9c25615c21902a9447ab03cc0a#OSW2b1c9c4b62385c4488e52fc40d8b7bbb"
    )


class Force(QuantityValue):
    """
    "Force" is an influence that causes mass to accelerate. It may be experienced as a lift, a push, or a pull. Force is defined by Newton's Second Law as $F = m \times a $, where $F$ is force, $m$ is mass and $a$ is acceleration. Net force is mathematically equal to the time rate of change of the momentum of the body on which it acts. Since momentum is a vector quantity (has both a magnitude and direction), force also is a vector quantity.
    """

    type: Optional[Any] = ["Category:OSW1b832c1a42c055eb9669bb0cdda18d7f"]
    unit: Optional[ForceUnit] = Field(ForceUnit.newton, title="ForceUnit")



class ThermalDiffusionCoefficientUnit(UnitEnum):
    meter_squared_per_second = "Item:OSW20b837bfd2fa5c3abc86347ce702f27c"
    milli_meter_squared_per_second = (
        "Item:OSW20b837bfd2fa5c3abc86347ce702f27c#OSW5db8f161eb8c59129cef62d84dd3309c"
    )
    centi_meter_squared_per_second = (
        "Item:OSW20b837bfd2fa5c3abc86347ce702f27c#OSW031bb99ee99a5794a24c66e6203c21db"
    )


class ThermalDiffusionCoefficient(QuantityValue):
    """
    The "Thermal Diffusion Coefficient" is .
    """

    type: Optional[Any] = ["Category:OSWe86c6ab0958a515da6b37bbec5a4c8e6"]
    unit: Optional[ThermalDiffusionCoefficientUnit] = Field(
        ThermalDiffusionCoefficientUnit.meter_squared_per_second,
        title="ThermalDiffusionCoefficientUnit",
    )



class LinearDensityUnit(UnitEnum):
    kilo_gram_per_meter = (
        "Item:OSW0429f89d17e6572fac6630caa443c336#OSW1e1793e6b72454f1a81b08eabc8272b7"
    )


class LinearDensity(QuantityValue):
    """
    The Linear density, linear mass density or linear mass is a measure of mass per unit of length, and it is a characteristic of strings or other one-dimensional objects.
    """

    type: Optional[Any] = ["Category:OSWfd1bbc6978425fe9869574ec4a5976a6"]
    unit: Optional[LinearDensityUnit] = Field(
        LinearDensityUnit.kilo_gram_per_meter, title="LinearDensityUnit"
    )



class MagneticMomentUnit(UnitEnum):
    joule_per_tesla = "Item:OSWd99c0ceb8ce951b6a513cd58955b69d2"


class MagneticMoment(QuantityValue):
    """
    "Magnetic Moment", for a magnetic dipole, is a vector quantity equal to the product of the current, the loop area, and the unit vector normal to the loop plane, the direction of which corresponds to the loop orientation. "Magnetic Moment" is also referred to as "Magnetic Area Moment", and is not to be confused with Magnetic Dipole Moment.
    """

    type: Optional[Any] = ["Category:OSW7d63568fd3d854268aba399d60e611ef"]
    unit: Optional[MagneticMomentUnit] = Field(
        MagneticMomentUnit.joule_per_tesla, title="MagneticMomentUnit"
    )



class TorquePerAngleUnit(UnitEnum):
    meter_newton_per_radian = "Item:OSWcf35571886b95c2c889f076d7dab41dd"


class TorquePerAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TorquePerAngle'
    """

    type: Optional[Any] = ["Category:OSW38077176ba8a52f7a9f401d782b4ffa8"]
    unit: Optional[TorquePerAngleUnit] = Field(
        TorquePerAngleUnit.meter_newton_per_radian, title="TorquePerAngleUnit"
    )



class MolarEntropyUnit(UnitEnum):
    joule_per_kelvin_per_mole = "Item:OSW6d40ac4bdbc950ec9290f6a47ce23d20"


class MolarEntropy(QuantityValue):
    """
    The "Standard Molar Entropy" is the entropy content of one mole of substance, under standard conditions (not standard temperature and pressure STP).
    """

    type: Optional[Any] = ["Category:OSW78bb22c171075ca781ec3c9fff9991ea"]
    unit: Optional[MolarEntropyUnit] = Field(
        MolarEntropyUnit.joule_per_kelvin_per_mole, title="MolarEntropyUnit"
    )



class CapacitanceUnit(UnitEnum):
    farad = "Item:OSWa1b4f9da4183543a8161e3fe99751be2"
    pico_farad = (
        "Item:OSWa1b4f9da4183543a8161e3fe99751be2#OSWea22beb7c14350cfb4a8029430e0a9e3"
    )
    milli_farad = (
        "Item:OSWa1b4f9da4183543a8161e3fe99751be2#OSW233c7ca125dc5092bdc69b05723ba75b"
    )
    micro_farad = (
        "Item:OSWa1b4f9da4183543a8161e3fe99751be2#OSW3690c26e937c55f1aeb3dcba3c5d79f4"
    )
    nano_farad = (
        "Item:OSWa1b4f9da4183543a8161e3fe99751be2#OSW2c99e79b872e50d7a3cdb3b0614bbb1d"
    )
    atto_farad = (
        "Item:OSWa1b4f9da4183543a8161e3fe99751be2#OSW328bea7c368659c0ab2729ace2604ebc"
    )


class Capacitance(QuantityValue):
    """
    "Capacitance" is the ability of a body to hold an electrical charge; it is quantified as the amount of electric charge stored for a given electric potential. Capacitance is a scalar-valued quantity.
    """

    type: Optional[Any] = ["Category:OSW6bad72aa82835ea49eea9bb061beae80"]
    unit: Optional[CapacitanceUnit] = Field(
        CapacitanceUnit.farad, title="CapacitanceUnit"
    )



class ElectricCurrentDensityUnit(UnitEnum):
    ampere_per_meter_squared = "Item:OSW2b1e97f1edd650c088abbe8896fe0333"
    mega_ampere_per_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWd0a4ce0cc105550b9bcbc416589a1b85"
    )
    kilo_ampere_per_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWa80d9ac2c0455902ab9531512c9b7667"
    )
    ampere_per_milli_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSW8d7d0b57aaba5f8a8f40e8bacc5cb2f6"
    )
    ampere_per_centi_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWec1a540d03745760af1d26077e9d762e"
    )


class ElectricCurrentDensity(QuantityValue):
    """
    "Electric Current Density" is a measure of the density of flow of electric charge; it is the electric current per unit area of cross section. Electric current density is a vector-valued quantity. Electric current, $I$, through a surface $S$ is defined as $I = \int_S J \cdot e_n dA$, where $e_ndA$ is the vector surface element.
    """

    type: Optional[Any] = ["Category:OSWb43cba22fb1d5124bd569a3e18826b1f"]
    unit: Optional[ElectricCurrentDensityUnit] = Field(
        ElectricCurrentDensityUnit.ampere_per_meter_squared,
        title="ElectricCurrentDensityUnit",
    )



class SpecificHeatCapacityAtConstantVolumeUnit(UnitEnum):
    joule_per_Celsius_per_kilo_gram = (
        "Item:OSW93d8b6e516fd54f09d483dee1278e3a8#OSWa0cd208ccfa759388597f5f9ff5c69fc"
    )


class SpecificHeatCapacityAtConstantVolume(QuantityValue):
    """
    Specific heat per constant volume.
    """

    type: Optional[Any] = ["Category:OSW9cfbce99c0f65684a82590ef1d71f111"]
    unit: Optional[SpecificHeatCapacityAtConstantVolumeUnit] = Field(
        SpecificHeatCapacityAtConstantVolumeUnit.joule_per_Celsius_per_kilo_gram,
        title="SpecificHeatCapacityAtConstantVolumeUnit",
    )



class TorquePerLengthUnit(UnitEnum):
    newton = "Item:OSW9ed7c23bcd215a00b2da55e18e9d1238"
    kilo_newton = (
        "Item:OSW9ed7c23bcd215a00b2da55e18e9d1238#OSWd300f757ad1657c091ae9664d0e6d51f"
    )


class TorquePerLength(QuantityValue):
    """
    This is an autogenerated partial class definition of 'TorquePerLength'
    """

    type: Optional[Any] = ["Category:OSW18e8102a660f5d4eb91c9b70c3083a04"]
    unit: Optional[TorquePerLengthUnit] = Field(
        TorquePerLengthUnit.newton, title="TorquePerLengthUnit"
    )



class SpeedUnit(UnitEnum):
    meter_per_second = "Item:OSW78331234e1a15aeebd8b0caa71201939"
    centi_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWd094e4cfd62c52248aad5ef87c19fb7d"
    )
    micro_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSWfc9fca27ba5b543c8780521b4af39189"
    )
    milli_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW4937ac85021f506cb7ba3958f2216bd1"
    )
    kilo_meter_per_second = (
        "Item:OSW78331234e1a15aeebd8b0caa71201939#OSW9f12ce12bc725cd59791265e2e480fd2"
    )


class Speed(QuantityValue):
    """
    Speed is the magnitude of velocity.
    """

    type: Optional[Any] = ["Category:OSW29b1dc01984d568f84c03e03ed2ed731"]
    unit: Optional[SpeedUnit] = Field(SpeedUnit.meter_per_second, title="SpeedUnit")



class ElectromagneticEnergyDensityUnit(UnitEnum):
    joule_per_meter_cubed = "Item:OSW9ea4bf89c42b56728392f1c55639ac18"
    mega_joule_per_meter_cubed = (
        "Item:OSW9ea4bf89c42b56728392f1c55639ac18#OSW7044da5ba4b45554b3acc6c6f3fc3624"
    )


class ElectromagneticEnergyDensity(QuantityValue):
    """
    $\textit{Electromagnetic Energy Density}$, also known as the $\color{indigo} {\text{Volumic Electromagnetic Energy}}$, is the energy associated with an electromagnetic field, per unit volume of the field.
    """

    type: Optional[Any] = ["Category:OSWd762c41183225469b74fb0626b36aa70"]
    unit: Optional[ElectromagneticEnergyDensityUnit] = Field(
        ElectromagneticEnergyDensityUnit.joule_per_meter_cubed,
        title="ElectromagneticEnergyDensityUnit",
    )



class SpecificActivityUnit(UnitEnum):
    becquerel_per_kilo_gram = "Item:OSW03b25e9a7cef5adeb7f3d5f82115dfc3"
    milli_becquerel_per_kilo_gram = (
        "Item:OSW03b25e9a7cef5adeb7f3d5f82115dfc3#OSWc896c96c6de8521181daee0118de2c5b"
    )
    micro_becquerel_per_kilo_gram = (
        "Item:OSW03b25e9a7cef5adeb7f3d5f82115dfc3#OSW23b3668ed7d3501da40aaa0a4e9f765e"
    )


class SpecificActivity(QuantityValue):
    """
    The "Specific Activity" is the number of decays per unit time of a radioactive sample. The SI unit of radioactive activity is the becquerel (Bq), in honor of the scientist Henri Becquerel.
    """

    type: Optional[Any] = ["Category:OSWeb633138f3155fd09a5fa2b6ac5b5bc2"]
    unit: Optional[SpecificActivityUnit] = Field(
        SpecificActivityUnit.becquerel_per_kilo_gram, title="SpecificActivityUnit"
    )



class LineicPowerUnit(UnitEnum):
    watt_per_meter = "Item:OSW4cf53c813d36501db82ba5b6ac1a48bf"


class LineicPower(QuantityValue):
    """
    Leistung dividiert durch die zugehörige Länge
    """

    type: Optional[Any] = ["Category:OSWeb347cbbd41e5a9aa876a7024a75a33b"]
    unit: Optional[LineicPowerUnit] = Field(
        LineicPowerUnit.watt_per_meter, title="LineicPowerUnit"
    )



class ElectricChargePerAreaUnit(UnitEnum):
    coulomb_per_meter_squared = "Item:OSW1f38c1c62b2850deb24c1c3afccfc239"
    mega_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSW344d47f96cd55fe89e73f85cb1054450"
    )
    coulomb_per_milli_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSW596e6e9224085a35b395fc84aa4edde8"
    )
    micro_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSWea3f16aa263f52dc941e62b9c510ade5"
    )
    coulomb_per_centi_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSWf6450e8adb145e3a8cc3104122cdc667"
    )
    kilo_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSW6314b9832a355b7cab3616f5d08c4165"
    )
    milli_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSWaace10bd10b5537299ad0548738e0b5e"
    )


class ElectricChargePerArea(QuantityValue):
    """
    In electromagnetism, charge density is a measure of electric charge per unit volume of space, in one, two or three dimensions. More specifically: the linear, surface, or volume charge density is the amount of electric charge per unit length, surface area, or volume, respectively. The respective SI units are $C \cdot m^{-1}$, $C \cdot m^{-2}$ or $C \cdot m^{-3}$.
    """

    type: Optional[Any] = ["Category:OSW4f0b36aedcac5f4dafcc0eaec8eb86dd"]
    unit: Optional[ElectricChargePerAreaUnit] = Field(
        ElectricChargePerAreaUnit.coulomb_per_meter_squared,
        title="ElectricChargePerAreaUnit",
    )



class MassAbsorptionCoefficientUnit(UnitEnum):
    meter_squared_per_kilo_gram = (
        "Item:OSWd7015166d39d5cae866a40eac3d51896#OSWc811db362efa5d33a49b56ffdd77e54d"
    )


class MassAbsorptionCoefficient(QuantityValue):
    """
    The mass absorption coefficient is the linear absorption coefficient divided by the density of the absorber.
    """

    type: Optional[Any] = ["Category:OSW4270a516cdbe5466abeea6638b402fea"]
    unit: Optional[MassAbsorptionCoefficientUnit] = Field(
        MassAbsorptionCoefficientUnit.meter_squared_per_kilo_gram,
        title="MassAbsorptionCoefficientUnit",
    )



class CoercivityUnit(UnitEnum):
    ampere_per_meter = "Item:OSW21e01a5082e35d5cbcf741df0a054cee"
    ampere_per_milli_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSW81d243ef653b5b6b890b1102d37d6d78"
    )
    milli_ampere_per_milli_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSWe385b197cb0e581d8e25ce1ec9a73c7a"
    )
    kilo_ampere_per_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSWe299bb79004b52b3a4c9f8a739b881bf"
    )
    ampere_per_centi_meter = (
        "Item:OSW21e01a5082e35d5cbcf741df0a054cee#OSW8d315234960451fa895c98b88e9f1b28"
    )


class Coercivity(QuantityValue):
    """
    $\textit{Coercivity}$, also referred to as $\textit{Coercive Field Strength}$, is the magnetic field strength to be applied to bring the magnetic flux density in a substance from its remaining magnetic flux density to zero. This is defined as the coercive field strength in a substance when either the magnetic flux density or the magnetic polarization and magnetization is brought from its value at magnetic saturation to zero by monotonic reduction of the applied magnetic field strength. The quantity which is brought to zero should be stated, and the appropriate symbol used: $H_{cB}$, $H_{cJ}$ or $H_{cM}$ for the coercivity relating to the magnetic flux density, the magnetic polarization or the magnetization respectively, where $H_{cJ} = H_{cM}$.
    """

    type: Optional[Any] = ["Category:OSWaa1087e428445c44b8c91a4c7ca76806"]
    unit: Optional[CoercivityUnit] = Field(
        CoercivityUnit.ampere_per_meter, title="CoercivityUnit"
    )



class BodyMassIndexUnit(UnitEnum):
    kilo_gram_per_meter_squared = (
        "Item:OSWb93e608c86fd5480a5de9cd1b3e9ea22#OSW86b6ab5f70aa5624be17645333d53d51"
    )


class BodyMassIndex(QuantityValue):
    """
    $\textit{Body Mass Index}$, BMI, is an index of weight for height, calculated as: $BMI = \frac{M_{body}}{H^2}$, where $M_{body}$ is body mass in kg, and $H$ is height in metres. The BMI has been used as a guideline for defining whether a person is overweight because it minimizes the effect of height, but it does not take into consideration other important factors, such as age and body build. The BMI has also been used as an indicator of obesity on the assumption that the higher the index, the greater the level of body fat.
    """

    type: Optional[Any] = ["Category:OSW6b1c18cb5a6e50519e026012231b9603"]
    unit: Optional[BodyMassIndexUnit] = Field(
        BodyMassIndexUnit.kilo_gram_per_meter_squared, title="BodyMassIndexUnit"
    )



class PermeabilityUnit(UnitEnum):
    henry_per_meter = "Item:OSW12866a70d0a25caa932f30e99aceaf78"
    micro_henry_per_meter = (
        "Item:OSW12866a70d0a25caa932f30e99aceaf78#OSW4c3c9d5890b9500c91bb519b11dbdd34"
    )
    nano_henry_per_meter = (
        "Item:OSW12866a70d0a25caa932f30e99aceaf78#OSW4c9c95ef060e5f40a9169574264d38b1"
    )


class Permeability(QuantityValue):
    """
    This is an autogenerated partial class definition of 'Permeability'
    """

    type: Optional[Any] = ["Category:OSW0f7b761273895e3886f0584b3b8197b1"]
    unit: Optional[PermeabilityUnit] = Field(
        PermeabilityUnit.henry_per_meter, title="PermeabilityUnit"
    )



class ElectricPolarizationUnit(UnitEnum):
    coulomb_per_meter_squared = "Item:OSW1f38c1c62b2850deb24c1c3afccfc239"
    mega_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSW344d47f96cd55fe89e73f85cb1054450"
    )
    coulomb_per_milli_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSW596e6e9224085a35b395fc84aa4edde8"
    )
    micro_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSWea3f16aa263f52dc941e62b9c510ade5"
    )
    coulomb_per_centi_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSWf6450e8adb145e3a8cc3104122cdc667"
    )
    kilo_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSW6314b9832a355b7cab3616f5d08c4165"
    )
    milli_coulomb_per_meter_squared = (
        "Item:OSW1f38c1c62b2850deb24c1c3afccfc239#OSWaace10bd10b5537299ad0548738e0b5e"
    )


class ElectricPolarization(QuantityValue):
    """
    "Electric Polarization" is the relative shift of positive and negative electric charge in opposite directions within an insulator, or dielectric, induced by an external electric field. Polarization occurs when an electric field distorts the negative cloud of electrons around positive atomic nuclei in a direction opposite the field. This slight separation of charge makes one side of the atom somewhat positive and the opposite side somewhat negative. In some materials whose molecules are permanently polarized by chemical forces, such as water molecules, some of the polarization is caused by molecules rotating into the same alignment under the influence of the electric field. One of the measures of polarization is electric dipole moment, which equals the distance between the slightly shifted centres of positive and negative charge multiplied by the amount of one of the charges. Polarization P in its quantitative meaning is the amount of dipole moment p per unit volume V of a polarized material, P = p/V.
    """

    type: Optional[Any] = ["Category:OSWb2f047e5e8fe5cc8bc80399216214caa"]
    unit: Optional[ElectricPolarizationUnit] = Field(
        ElectricPolarizationUnit.coulomb_per_meter_squared,
        title="ElectricPolarizationUnit",
    )



class ExpansionRatioUnit(UnitEnum):
    per_kelvin = "Item:OSW33dfda3d4dea57d192d02eecdbc09b86"


class ExpansionRatio(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ExpansionRatio'
    """

    type: Optional[Any] = ["Category:OSWa3a8179bb49f5fafa9ff680f4d7f9f34"]
    unit: Optional[ExpansionRatioUnit] = Field(
        ExpansionRatioUnit.per_kelvin, title="ExpansionRatioUnit"
    )



class PressureLossPerLengthUnit(UnitEnum):
    kilo_gram_per_meter_squared_per_second_squared = (
        "Item:OSW876a1c66fd4c5fda86f129d3b65a1b98"
    )


class PressureLossPerLength(QuantityValue):
    """
    "Pressure Loss per Length" refers to the power lost in overcoming the friction between two moving surfaces. Also referred to as "Friction Loss".
    """

    type: Optional[Any] = ["Category:OSW9315ab4cdde456b4948e73cc6ba050b1"]
    unit: Optional[PressureLossPerLengthUnit] = Field(
        PressureLossPerLengthUnit.kilo_gram_per_meter_squared_per_second_squared,
        title="PressureLossPerLengthUnit",
    )



class RecombinationCoefficientUnit(UnitEnum):
    meter_cubed_per_second = "Item:OSW4ed5503a56ab514ab3d925287da52a95"
    centi_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSWacda1333cb6958069dc83172f3a047db"
    )
    deci_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSW58c067fb208b5294899599809141c3ff"
    )


class RecombinationCoefficient(QuantityValue):
    """
    The "Recombination Coefficient" is the rate of recombination of positive ions with electrons or negative ions in a gas, per unit volume, divided by the product of the number of positive ions per unit volume and the number of electrons or negative ions per unit volume.
    """

    type: Optional[Any] = ["Category:OSW518bf0736bae513a83f161f597ddc074"]
    unit: Optional[RecombinationCoefficientUnit] = Field(
        RecombinationCoefficientUnit.meter_cubed_per_second,
        title="RecombinationCoefficientUnit",
    )



class SpecificEntropyUnit(UnitEnum):
    joule_per_Celsius_per_kilo_gram = (
        "Item:OSW93d8b6e516fd54f09d483dee1278e3a8#OSWa0cd208ccfa759388597f5f9ff5c69fc"
    )


class SpecificEntropy(QuantityValue):
    """
    "Specific Entropy" is entropy per unit of mass.
    """

    type: Optional[Any] = ["Category:OSW96b8069ea0bd588892e7efe11651bcf1"]
    unit: Optional[SpecificEntropyUnit] = Field(
        SpecificEntropyUnit.joule_per_Celsius_per_kilo_gram, title="SpecificEntropyUnit"
    )



class LuminanceUnit(UnitEnum):
    candela_per_meter_squared = "Item:OSW4f047e2da1fc5ea497c9e22eb8e98ce5"


class Luminance(QuantityValue):
    """
    Luminance is a photometric measure of the luminous intensity per unit area of light travelling in a given direction. It describes the amount of light that passes through or is emitted from a particular area, and falls within a given solid angle.
    """

    type: Optional[Any] = ["Category:OSWfad284976682566cab9ebd9d6bd15711"]
    unit: Optional[LuminanceUnit] = Field(
        LuminanceUnit.candela_per_meter_squared, title="LuminanceUnit"
    )



class AngularImpulseUnit(UnitEnum):
    joule_second = "Item:OSWf045a04750e15ea2b152fb3bfebf162a"
    atto_joule_second = (
        "Item:OSWf045a04750e15ea2b152fb3bfebf162a#OSW3eaa66dd20f856fe9a5c4199bc0a1ea4"
    )


class AngularImpulse(QuantityValue):
    """
    The Angular Impulse, also known as angular momentum, is the moment of linear momentum around a point. It is defined as$H = \int Mdt$, where $M$ is the moment of force and $t$ is time.
    """

    type: Optional[Any] = ["Category:OSW140347dd94e6593aaea4daf9a1264a0a"]
    unit: Optional[AngularImpulseUnit] = Field(
        AngularImpulseUnit.joule_second, title="AngularImpulseUnit"
    )



class MagneticAreaMomentUnit(UnitEnum):
    joule_per_tesla = "Item:OSWd99c0ceb8ce951b6a513cd58955b69d2"


class MagneticAreaMoment(QuantityValue):
    """
    "Magnetic Area Moment", for a magnetic dipole, is a vector quantity equal to the product of the current, the loop area, and the unit vector normal to the loop plane, the direction of which corresponds to the loop orientation. "Magnetic Area Moment" is also referred to as "Magnetic Moment".
    """

    type: Optional[Any] = ["Category:OSW25caa8958ec05221a2bd22dbef7b9074"]
    unit: Optional[MagneticAreaMomentUnit] = Field(
        MagneticAreaMomentUnit.joule_per_tesla, title="MagneticAreaMomentUnit"
    )



class MomentOfForceUnit(UnitEnum):
    meter_newton = "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3"
    deci_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW83f4a238c5875e3587f45071e11aaaa3"
    )
    centi_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSWb7de5ae5a2f05221be05e0bf2aa74cb9"
    )
    meter_milli_newton = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW62f7907222b855ffb1920944af234145"
    )
    kilo_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSWba8c33e36b605a5083b4d9f87e89d04a"
    )
    meter_micro_newton = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSWcc1060f0faed597fbef0006b2c6de73d"
    )
    mega_newton_meter = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW48e50fcb919e57d99158eb2308baed11"
    )
    centi_meter_newton = (
        "Item:OSW599c5384bf7a5de7b8cee8b2e94c39e3#OSW4a6a4e3488695755a9b81d0947b0f85a"
    )


class MomentOfForce(QuantityValue):
    """
    Moment of force (often just moment) is the tendency of a force to twist or rotate an object.
    """

    type: Optional[Any] = ["Category:OSW305a18e416d6519e8683eaf9dfce1dec"]
    unit: Optional[MomentOfForceUnit] = Field(
        MomentOfForceUnit.meter_newton, title="MomentOfForceUnit"
    )



class TotalAtomicStoppingPowerUnit(UnitEnum):
    joule_meter_squared = "Item:OSW56a0d2c5894a539dab6c6581082cf5ae"


class TotalAtomicStoppingPower(QuantityValue):
    """
    The "Total Atomic Stopping Power" for an ionizing particle passing through an element, is the particle's energy loss per atom within a unit area normal to the particle's path; equal to the linear energy transfer (energy loss per unit path length) divided by the number of atoms per unit volume.
    """

    type: Optional[Any] = ["Category:OSW261c913da725592392a603767e4f9c32"]
    unit: Optional[TotalAtomicStoppingPowerUnit] = Field(
        TotalAtomicStoppingPowerUnit.joule_meter_squared,
        title="TotalAtomicStoppingPowerUnit",
    )



class ConductanceUnit(UnitEnum):
    siemens = "Item:OSW46249e4c237d546198d98bff0b9d5e93"
    milli_siemens = (
        "Item:OSW46249e4c237d546198d98bff0b9d5e93#OSW8253047fc4835d79b0f31baf3b96182d"
    )
    kilo_siemens = (
        "Item:OSW46249e4c237d546198d98bff0b9d5e93#OSW35746906e9d051c39bdeebdf5736c2ba"
    )
    micro_siemens = (
        "Item:OSW46249e4c237d546198d98bff0b9d5e93#OSWfd5a12b202d2534c9cb0844fb6c4f15e"
    )


class Conductance(QuantityValue):
    """
    $\textit{Conductance}$, for a resistive two-terminal element or two-terminal circuit with terminals A and B, quotient of the electric current i in the element or circuit by the voltage $u_{AB}$ between the terminals: $G = \frac{1}{R}$, where the electric current is taken as positive if its direction is from A to B and negative in the opposite case. The conductance of an element or circuit is the inverse of its resistance.
    """

    type: Optional[Any] = ["Category:OSW0e1e7031084d5e20b42b5ceba993d916"]
    unit: Optional[ConductanceUnit] = Field(
        ConductanceUnit.siemens, title="ConductanceUnit"
    )



class PowerAreaPerSolidAngleUnit(UnitEnum):
    meter_squared_watt_per_steradian = "Item:OSW21cf512b048358628e8ce57f4cecb9cc"


class PowerAreaPerSolidAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'PowerAreaPerSolidAngle'
    """

    type: Optional[Any] = ["Category:OSWd6e7af5891785a8eb9b54036c37a8bcb"]
    unit: Optional[PowerAreaPerSolidAngleUnit] = Field(
        PowerAreaPerSolidAngleUnit.meter_squared_watt_per_steradian,
        title="PowerAreaPerSolidAngleUnit",
    )



class CurrentLinkageUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class CurrentLinkage(QuantityValue):
    """
    "Current Linkage" is the net electric current through a surface delimited by a closed loop.
    """

    type: Optional[Any] = ["Category:OSW9c76ad47f40350a2884c90c49786ec6f"]
    unit: Optional[CurrentLinkageUnit] = Field(
        CurrentLinkageUnit.ampere, title="CurrentLinkageUnit"
    )



class TorsionalSpringConstantUnit(UnitEnum):
    meter_newton_per_radian = "Item:OSWcf35571886b95c2c889f076d7dab41dd"


class TorsionalSpringConstant(QuantityValue):
    """
    A torsional spring constant is a measure of the stiffness of a torsional spring, which is a type of spring that experiences twisting or torque rather than compression or extension. It is typically measured in newton-meters per radian (N·m/rad) and is used to calculate the amount of torque required to twist a spring a certain amount. It is related to the spring's geometry, material properties, and manufacturing process. #,#Quotient Drehmoment zur elastischen Verformung einer Drehfeder durch den zugehörigen Drehwinkel
    """

    type: Optional[Any] = ["Category:OSWca8833707e3c5a778696fa2c53877a28"]
    unit: Optional[TorsionalSpringConstantUnit] = Field(
        TorsionalSpringConstantUnit.meter_newton_per_radian,
        title="TorsionalSpringConstantUnit",
    )



class MassConcentrationOfWaterUnit(UnitEnum):
    kilo_gram_per_meter_cubed = (
        "Item:OSW9161ae8b61ca56a687f8db32bdf2ddd3#OSW52992dd0def35dc9ae8bd6b5010d8ee8"
    )


class MassConcentrationOfWater(QuantityValue):
    """
    Mass Concentration of Water is one of a number of Concentration quantities defined by ISO 80000.
    """

    type: Optional[Any] = ["Category:OSWd6ce0df1d9eb5b72991449f83965927c"]
    unit: Optional[MassConcentrationOfWaterUnit] = Field(
        MassConcentrationOfWaterUnit.kilo_gram_per_meter_cubed,
        title="MassConcentrationOfWaterUnit",
    )



class ElectricCurrentPerAngleUnit(UnitEnum):
    ampere_per_radian = "Item:OSW3aba7ea2f6a552d4a9762e4b654d32a1"


class ElectricCurrentPerAngle(QuantityValue):
    """
    This is an autogenerated partial class definition of 'ElectricCurrentPerAngle'
    """

    type: Optional[Any] = ["Category:OSWf46a3d86783554a19d5bce2a41a98552"]
    unit: Optional[ElectricCurrentPerAngleUnit] = Field(
        ElectricCurrentPerAngleUnit.ampere_per_radian,
        title="ElectricCurrentPerAngleUnit",
    )



class SpecificHeatCapacityAtSaturationUnit(UnitEnum):
    joule_per_Celsius_per_kilo_gram = (
        "Item:OSW93d8b6e516fd54f09d483dee1278e3a8#OSWa0cd208ccfa759388597f5f9ff5c69fc"
    )


class SpecificHeatCapacityAtSaturation(QuantityValue):
    """
    Specific heat per constant volume.
    """

    type: Optional[Any] = ["Category:OSW4500771e3381532098001c704d0b9cb1"]
    unit: Optional[SpecificHeatCapacityAtSaturationUnit] = Field(
        SpecificHeatCapacityAtSaturationUnit.joule_per_Celsius_per_kilo_gram,
        title="SpecificHeatCapacityAtSaturationUnit",
    )



class PlaneAngleUnit(UnitEnum):
    radian = "Item:OSW6b270053305955a89f37c50637fc7aeb"
    micro_radian = (
        "Item:OSW6b270053305955a89f37c50637fc7aeb#OSW80a423e717c3546f8085fa732b37409e"
    )
    milli_radian = (
        "Item:OSW6b270053305955a89f37c50637fc7aeb#OSW8fb3bf64b8f751498553ead8995be20c"
    )


class PlaneAngle(QuantityValue):
    """
    An angle formed by two straight lines (in the same plane) angle - the space between two lines or planes that intersect; the inclination of one line to another; measured in degrees or radians
    """

    type: Optional[Any] = ["Category:OSWcfa8c1748f3b586e9a0304ab1e2dbc41"]
    unit: Optional[PlaneAngleUnit] = Field(
        PlaneAngleUnit.radian, title="PlaneAngleUnit"
    )



class EntropyUnit(UnitEnum):
    joule_per_kelvin = "Item:OSW501738b1f645568c9c4fb6da844439c7"
    kilo_joule_per_kelvin = (
        "Item:OSW501738b1f645568c9c4fb6da844439c7#OSW7b31ddba89fc5359972c09eda7f30683"
    )
    mega_joule_per_kelvin = (
        "Item:OSW501738b1f645568c9c4fb6da844439c7#OSWf8925d2e60865f589809095c9e172dbe"
    )


class Entropy(QuantityValue):
    """
    When a small amount of heat $dQ$ is received by a system whose thermodynamic temperature is $T$, the entropy of the system increases by $dQ/T$, provided that no irreversible change takes place in the system.
    """

    type: Optional[Any] = ["Category:OSWcb71f0cf941a58709eace6b2c98ebeda"]
    unit: Optional[EntropyUnit] = Field(
        EntropyUnit.joule_per_kelvin, title="EntropyUnit"
    )



class InverseLengthTemperatureUnit(UnitEnum):
    per_kelvin_per_meter = "Item:OSWf56de776e1935d7da1fc50db7cd12490"


class InverseLengthTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseLengthTemperature'
    """

    type: Optional[Any] = ["Category:OSW0f94186c90c85d2699585af6b6985d2c"]
    unit: Optional[InverseLengthTemperatureUnit] = Field(
        InverseLengthTemperatureUnit.per_kelvin_per_meter,
        title="InverseLengthTemperatureUnit",
    )



class Permeability(QuantityValue):
    """
    $\textit{Permeability}$ is the degree of magnetization of a material that responds linearly to an applied magnetic field.
      In general permeability is a tensor-valued quantity.
      The definition given applies to an isotropic medium.
      For an anisotropic medium permeability is a second order tensor.
      In electromagnetism, permeability is the measure of the ability of a material to support the formation of a magnetic field within itself.
      In other words, it is the degree of magnetization that a material obtains in response to an applied magnetic field.
      Magnetic permeability is typically represented by the Greek letter $\mu$.
      The term was coined in September, 1885 by Oliver Heaviside.
      The reciprocal of magnetic permeability is $\textit{Magnetic Reluctivity}$.
    """

    type: Optional[Any] = ["Category:OSW3f643ed2dc235d8ab1c823dfa357c16b"]
    unit: Optional[PermeabilityUnit] = Field(
        PermeabilityUnit.henry_per_meter, title="PermeabilityUnit"
    )



class RotationalFrequencyUnit(UnitEnum):
    hertz = "Item:OSW7496c09c41b154bdba82f6d09195cae5"
    mega_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSWb5d0dd4f66285e15af5977a1b77d5daa"
    )
    kilo_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSWfbbfa62ac8095c5bb37ea9f22ab121dd"
    )
    giga_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSW37c66b2e350050d891107e427a1c0210"
    )
    tera_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSW5860049cdfae5d64abcd7bb8ace55540"
    )


class RotationalFrequency(QuantityValue):
    """
    IfcRotationalFrequencyMeasure is a measure of the number of cycles that an item revolves in unit time. Usually measured in cycles/s.
    """

    type: Optional[Any] = ["Category:OSWa57dc71706f75ba7995a8eebdcea18da"]
    unit: Optional[RotationalFrequencyUnit] = Field(
        RotationalFrequencyUnit.hertz, title="RotationalFrequencyUnit"
    )



class ScalarMagneticPotentialUnit(UnitEnum):
    second_volt_per_meter = "Item:OSWf63c15f03855534fabdc39bb5403d1ff"


class ScalarMagneticPotential(QuantityValue):
    """
    "Scalar Magnetic Potential" is the scalar potential of an irrotational magnetic field strength. The negative of the gradient of the scalar magnetic potential is the irrotational magnetic field strength. The magnetic scalar potential is not unique since any constant scalar field can be added to it without changing its gradient.
    """

    type: Optional[Any] = ["Category:OSWfc761e5fae6951f2a4f563e06b6cfc85"]
    unit: Optional[ScalarMagneticPotentialUnit] = Field(
        ScalarMagneticPotentialUnit.second_volt_per_meter,
        title="ScalarMagneticPotentialUnit",
    )



class MassConcentrationOfWaterVapourUnit(UnitEnum):
    kilo_gram_per_meter_cubed = (
        "Item:OSW9161ae8b61ca56a687f8db32bdf2ddd3#OSW52992dd0def35dc9ae8bd6b5010d8ee8"
    )


class MassConcentrationOfWaterVapour(QuantityValue):
    """
    Mass Concentration of Water is one of a number of Concentration quantities defined by ISO 80000.
    """

    type: Optional[Any] = ["Category:OSW73df0db8ab3656d7927bc38db277a50e"]
    unit: Optional[MassConcentrationOfWaterVapourUnit] = Field(
        MassConcentrationOfWaterVapourUnit.kilo_gram_per_meter_cubed,
        title="MassConcentrationOfWaterVapourUnit",
    )



class MassUnit(UnitEnum):
    kilo_gram = (
        "Item:OSW3c9bf4c3682f5a52b6e99f7ad7949903#OSWda255533fa615a42b08ddb7aaa8236f0"
    )


class Mass(QuantityValue):
    """
    In physics, mass, more specifically inertial mass, can be defined as a quantitative measure of an object's resistance to acceleration. The SI unit of mass is the kilogram ($kg$)
    """

    type: Optional[Any] = ["Category:OSWe9be062de2d15d10891397a18212f920"]
    unit: Optional[MassUnit] = Field(MassUnit.kilo_gram, title="MassUnit")



class ElectricChargeUnit(UnitEnum):
    coulomb = "Item:OSWb74ce812542f578fb6df2ecf9080fb32"
    deci_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW43d7083218b858a784ef5d19c42606ea"
    )
    atto_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW1010057c769a56eb975e76734b40a1a3"
    )
    zetta_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW43bcc13fe0d75ff7aa494e24507f4d3b"
    )
    deca_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW0dc82895087a55999831834657f5271c"
    )
    micro_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWaad8fcf05ad653449218daabfbf35641"
    )
    hecto_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW5f73734ea6a95b52b9800cf85ca23f55"
    )
    nano_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW39159f1f4ebe549581554b919caa87c9"
    )
    peta_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW90fb959a831b5b29bc86fdabb41679fb"
    )
    tera_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW868f3e7ae7985d7b9b31e1c28651024f"
    )
    femto_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWc9bf34efc99e5a6da522bedea2769891"
    )
    milli_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW130e4feb48905369a2b4f8549cf498cc"
    )
    mega_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWf9b7fd9f6d9a5b1ebbb7ac2adda29b10"
    )
    centi_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW616dce3dfe0055bd88ea35a440e65a2e"
    )
    pico_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW4c8584e32f38539293526c1db8fe6628"
    )
    yocto_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWc0aeba8244d654cf9cd85d525355f3c6"
    )
    zepto_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW736c323569ea5b37a7ca958e00a76396"
    )
    yotta_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWfede83a73c325b43ab83ccb35d723742"
    )
    kilo_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSW6af96f8a91725e68a767d9b96a70be03"
    )
    giga_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWcfbed671b98954a381651182a70a1b7c"
    )
    exa_coulomb = (
        "Item:OSWb74ce812542f578fb6df2ecf9080fb32#OSWed659a23620d591ca13a9fb09d45f602"
    )


class ElectricCharge(QuantityValue):
    """
    "Electric Charge" is a fundamental conserved property of some subatomic particles, which determines their electromagnetic interaction. Electrically charged matter is influenced by, and produces, electromagnetic fields. The electric charge on a body may be positive or negative. Two positively charged bodies experience a mutual repulsive force, as do two negatively charged bodies. A positively charged body and a negatively charged body experience an attractive force. Electric charge is carried by discrete particles and can be positive or negative. The sign convention is such that the elementary electric charge $e$, that is, the charge of the proton, is positive. The SI derived unit of electric charge is the coulomb.
    """

    type: Optional[Any] = ["Category:OSWb7248b1f04455ec99e6ff6e6b472d8de"]
    unit: Optional[ElectricChargeUnit] = Field(
        ElectricChargeUnit.coulomb, title="ElectricChargeUnit"
    )



class CubicElectricDipoleMomentPerSquareEnergyUnit(UnitEnum):
    coulomb_cubed_meter_per_joule_squared = "Item:OSWbf685bb28c9b5d15ab98238af18f1f74"


class CubicElectricDipoleMomentPerSquareEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'CubicElectricDipoleMomentPerSquareEnergy'
    """

    type: Optional[Any] = ["Category:OSWd39e579131ea5e829bcd150c6cf0a86c"]
    unit: Optional[CubicElectricDipoleMomentPerSquareEnergyUnit] = Field(
        CubicElectricDipoleMomentPerSquareEnergyUnit.coulomb_cubed_meter_per_joule_squared,
        title="CubicElectricDipoleMomentPerSquareEnergyUnit",
    )



class InverseEnergyUnit(UnitEnum):
    per_hour_per_kilo_volt_ampere = "Item:OSW98c14d48aecc52fdab52023fb924debd"


class InverseEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseEnergy'
    """

    type: Optional[Any] = ["Category:OSW0da38e7b53f15e1788cc4bbfbc4c6842"]
    unit: Optional[InverseEnergyUnit] = Field(
        InverseEnergyUnit.per_hour_per_kilo_volt_ampere, title="InverseEnergyUnit"
    )



class SpecificSurfaceAreaUnit(UnitEnum):
    meter_squared_per_kilo_gram = (
        "Item:OSWd7015166d39d5cae866a40eac3d51896#OSWc811db362efa5d33a49b56ffdd77e54d"
    )


class SpecificSurfaceArea(QuantityValue):
    """
    Specific surface area (SSA) is a property of solids defined as the total surface area (SA) of a material per unit mass, (with units of m²/kg or m²/g). It is a physical value that can be used to determine the type and properties of a material (e.g. soil or snow). It has a particular importance for adsorption, heterogeneous catalysis, and reactions on surfaces.
    """

    type: Optional[Any] = ["Category:OSW64f924217a41523d9fc5e51c4be68e08"]
    unit: Optional[SpecificSurfaceAreaUnit] = Field(
        SpecificSurfaceAreaUnit.meter_squared_per_kilo_gram,
        title="SpecificSurfaceAreaUnit",
    )



class StressOpticCoefficientUnit(UnitEnum):
    per_pascal = "Item:OSWf030abd4441d52a7a8c5f84950985ea4"


class StressOpticCoefficient(QuantityValue):
    """
    When a ray of light passes through a photoelastic material, its electromagnetic wave components are resolved along the two principal stress directions and each component experiences a different refractive index due to the birefringence. The difference in the refractive indices leads to a relative phase retardation between the two components. Assuming a thin specimen made of isotropic materials, where two-dimensional photoelasticity is applicable, the magnitude of the relative retardation is given by the stress-optic law Δ=((2πt)/λ)C(σ₁-σ₂), where Δ is the induced retardation, C is the stress-optic coefficient, t is the specimen thickness, λ is the vacuum wavelength, and σ₁ and σ₂ are the first and second principal stresses, respectively.
    """

    type: Optional[Any] = ["Category:OSW5079df5bd9085725aebd171ce0f1bc1b"]
    unit: Optional[StressOpticCoefficientUnit] = Field(
        StressOpticCoefficientUnit.per_pascal, title="StressOpticCoefficientUnit"
    )



class EnergyPerAreaElectricChargeUnit(UnitEnum):
    volt_per_meter_squared = "Item:OSW50e05e2d20e858f281ef0d396691ec1e"


class EnergyPerAreaElectricCharge(QuantityValue):
    """
    "Energy Per Area Electric Charge" is the amount of electric energy associated with a unit of area.
    """

    type: Optional[Any] = ["Category:OSWfad7c5659feb576d8be24a8dd5ec3d7a"]
    unit: Optional[EnergyPerAreaElectricChargeUnit] = Field(
        EnergyPerAreaElectricChargeUnit.volt_per_meter_squared,
        title="EnergyPerAreaElectricChargeUnit",
    )



class LengthTemperatureTimeUnit(UnitEnum):
    centi_meter_Celsius_second = "Item:OSW47b476c946d35bde93b5757a8e2d3d1b"


class LengthTemperatureTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'LengthTemperatureTime'
    """

    type: Optional[Any] = ["Category:OSW3d8035cbaa265d40a8e6cb6317c72700"]
    unit: Optional[LengthTemperatureTimeUnit] = Field(
        LengthTemperatureTimeUnit.centi_meter_Celsius_second,
        title="LengthTemperatureTimeUnit",
    )



class MagnetomotiveForceUnit(UnitEnum):
    ampere = "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec"
    pico_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWb59bf21962f75857965df77a55549178"
    )
    mega_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSWc611b97c5c4354059113fb8f17a26f2f"
    )
    kilo_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW49e59ce46e35588193327425fa1d89ab"
    )
    micro_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW771bd899c7045f84b282cc653efe6d28"
    )
    milli_ampere = (
        "Item:OSW0846b0dbcf495d5aab1172e4fb3bddec#OSW614e3543b8aa55a5b4aa87c9cd179703"
    )


class MagnetomotiveForce(QuantityValue):
    """
    $\text{Magnetomotive Force}$, also referred to as ($mmf$), is the ability of an electric circuit to produce magnetic flux.
      Just as the ability of a battery to produce electric current is called its electromotive force
      or emf, mmf is taken as the work required to move a unit magnet pole from any point through any path
      which links the electric circuit back the same point in the presence of the magnetic force produced
      by the electric current in the circuit.
    $\text{Magnetomotive Force}$ is the scalar line integral of the magnetic field strength along a closed path.
    """

    type: Optional[Any] = ["Category:OSW940166fa5c7053708125f0c10236d916"]
    unit: Optional[MagnetomotiveForceUnit] = Field(
        MagnetomotiveForceUnit.ampere, title="MagnetomotiveForceUnit"
    )



class MagneticFieldUnit(UnitEnum):
    tesla = "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0"
    micro_tesla = (
        "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0#OSW30a0158af5445fbc8b08c843d0a84d5a"
    )
    milli_tesla = (
        "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0#OSW490afd74306a568c858e46dd393110fe"
    )
    nano_tesla = (
        "Item:OSW1d9ac7ec48cc5b7da90e8c2d529d6df0#OSW7b67d49640c75e54b4906f4bd72b494b"
    )


class MagneticField(QuantityValue):
    """
    The Magnetic Field, denoted $B$, is a fundamental field in electrodynamics which characterizes the magnetic force exerted by electric currents.  It is closely related to the auxillary magnetic field H (see quantitykind:AuxillaryMagneticField).
    """

    type: Optional[Any] = ["Category:OSW71dc7977cd3a539889a4af664c2e02da"]
    unit: Optional[MagneticFieldUnit] = Field(
        MagneticFieldUnit.tesla, title="MagneticFieldUnit"
    )



class PhotonRadianceUnit(UnitEnum):
    per_meter_squared_per_second_per_steradian = (
        "Item:OSWb2f2150d25eb5a948de6ae5033a72afa"
    )


class PhotonRadiance(QuantityValue):
    """
    A measure of flux of photons per surface area per solid angle
    """

    type: Optional[Any] = ["Category:OSWcca5fb126c335044b494f4a9e7a34913"]
    unit: Optional[PhotonRadianceUnit] = Field(
        PhotonRadianceUnit.per_meter_squared_per_second_per_steradian,
        title="PhotonRadianceUnit",
    )



class MolarAttenuationCoefficientUnit(UnitEnum):
    meter_squared_per_mole = "Item:OSWf4a7837882ed5a0b9b128b2d067fc97b"


class MolarAttenuationCoefficient(QuantityValue):
    """
    "Molar Attenuation Coefficient" is a measurement of how strongly a chemical species or substance absorbs or scatters light at a given wavelength, per amount of substance.
    """

    type: Optional[Any] = ["Category:OSW56a827e5333052079e10f02eecf577ad"]
    unit: Optional[MolarAttenuationCoefficientUnit] = Field(
        MolarAttenuationCoefficientUnit.meter_squared_per_mole,
        title="MolarAttenuationCoefficientUnit",
    )



class LuminousFluxUnit(UnitEnum):
    lumen = "Item:OSW24fcc1bb84db5b3b951db598cddc1319"
    kilo_lumen = (
        "Item:OSW24fcc1bb84db5b3b951db598cddc1319#OSW15cb09d631d65ecbb0d1b54df9f2475e"
    )


class LuminousFlux(QuantityValue):
    """
    Luminous Flux or Luminous Power is the measure of the perceived power of light. It differs from radiant flux, the measure of the total power of light emitted, in that luminous flux is adjusted to reflect the varying sensitivity of the human eye to different wavelengths of light.
    """

    type: Optional[Any] = ["Category:OSWaee74c2e34ed58939c1ab03d0f115a0f"]
    unit: Optional[LuminousFluxUnit] = Field(
        LuminousFluxUnit.lumen, title="LuminousFluxUnit"
    )



class VolumetricFluxUnit(UnitEnum):
    milli_liter_per_centi_meter_squared_per_minute = (
        "Item:OSW832931cbeded5692a611f7752ee6cf4c"
    )


class VolumetricFlux(QuantityValue):
    """
    In fluid dynamics, the volumetric flux is the rate of volume flow across a unit area (m3·s−1·m−2).[Wikipedia]
    """

    type: Optional[Any] = ["Category:OSW5df3876a59235801acdf9ee4970f8324"]
    unit: Optional[VolumetricFluxUnit] = Field(
        VolumetricFluxUnit.milli_liter_per_centi_meter_squared_per_minute,
        title="VolumetricFluxUnit",
    )



class SpecificHeatVolumeUnit(UnitEnum):
    joule_per_kelvin_per_kilo_gram_per_meter_cubed = (
        "Item:OSWc06da5be651b56d993bef3fc05d91bd6"
    )


class SpecificHeatVolume(QuantityValue):
    """
    Specific heat per constant volume.
    """

    type: Optional[Any] = ["Category:OSW74026893cf1a50c48b24be5ed1ffd6d2"]
    unit: Optional[SpecificHeatVolumeUnit] = Field(
        SpecificHeatVolumeUnit.joule_per_kelvin_per_kilo_gram_per_meter_cubed,
        title="SpecificHeatVolumeUnit",
    )



class AreaPerLengthUnit(UnitEnum):
    meter = "Item:OSWf63766f7c83852d7a1d8e12deeee90c7"


class AreaPerLength(QuantityValue):
    """
    Measure used to indicate the surface area of structural steel per unit length of the steel part.
    """

    type: Optional[Any] = ["Category:OSWc579ba41d14059ce8527252f610fd8bf"]
    unit: Optional[AreaPerLengthUnit] = Field(
        AreaPerLengthUnit.meter, title="AreaPerLengthUnit"
    )



class MolarAngularMomentumUnit(UnitEnum):
    joule_second_per_mole = "Item:OSW82c440beaf0d5f4980a8f525e5313fe5"


class MolarAngularMomentum(QuantityValue):
    """
    This is an autogenerated partial class definition of 'MolarAngularMomentum'
    """

    type: Optional[Any] = ["Category:OSW692fa5ea3a1156a8b7a6332c9b1b1dce"]
    unit: Optional[MolarAngularMomentumUnit] = Field(
        MolarAngularMomentumUnit.joule_second_per_mole, title="MolarAngularMomentumUnit"
    )



class ParticleSourceDensityUnit(UnitEnum):
    per_meter_cubed_per_second = "Item:OSW804e40f82f4955ab8f1bd0c1e9e77d28"


class ParticleSourceDensity(QuantityValue):
    """
    "Particle Source Density" is the rate of production of particles in a 3D domain divided by the volume of that element.
    """

    type: Optional[Any] = ["Category:OSWfd24274b97b557ebad5fbc98060ffcf6"]
    unit: Optional[ParticleSourceDensityUnit] = Field(
        ParticleSourceDensityUnit.per_meter_cubed_per_second,
        title="ParticleSourceDensityUnit",
    )



class LuminousEfficacyUnit(UnitEnum):
    lumen_per_watt = "Item:OSW1df25fb7ecc057a7a5e4de01e46158b8"


class LuminousEfficacy(QuantityValue):
    """
    Luminous Efficacy is the ratio of luminous flux (in lumens) to power (usually measured in watts). Depending on context, the power can be either the radiant flux of the source's output, or it can be the total electric power consumed by the source.
    """

    type: Optional[Any] = ["Category:OSW64253eb92383544f9b7571c7e07cff76"]
    unit: Optional[LuminousEfficacyUnit] = Field(
        LuminousEfficacyUnit.lumen_per_watt, title="LuminousEfficacyUnit"
    )



class VolumeFlowRateUnit(UnitEnum):
    meter_cubed_per_second = "Item:OSW4ed5503a56ab514ab3d925287da52a95"
    centi_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSWacda1333cb6958069dc83172f3a047db"
    )
    deci_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSW58c067fb208b5294899599809141c3ff"
    )


class VolumeFlowRate(QuantityValue):
    """
    Volumetric Flow Rate, (also known as volume flow rate, rate of fluid flow or volume velocity) is the volume of fluid which passes through a given surface per unit time.
    """

    type: Optional[Any] = ["Category:OSWfa14092de387562aaacbb2a35059aa60"]
    unit: Optional[VolumeFlowRateUnit] = Field(
        VolumeFlowRateUnit.meter_cubed_per_second, title="VolumeFlowRateUnit"
    )



class ChemicalAffinityUnit(UnitEnum):
    joule_per_mole = "Item:OSW7e66beeef6b05637a554d3506d689000"
    kilo_joule_per_mole = (
        "Item:OSW7e66beeef6b05637a554d3506d689000#OSW23b10a54326955adb1862933713551f9"
    )


class ChemicalAffinity(QuantityValue):
    """
    In chemical physics and physical chemistry, "Chemical Affinity" is the electronic property by which dissimilar chemical species are capable of forming chemical compounds. Chemical affinity can also refer to the tendency of an atom or compound to combine by chemical reaction with atoms or compounds of unlike composition.
    """

    type: Optional[Any] = ["Category:OSW697915ca05ad53cc95b0f14a3fd3fe5d"]
    unit: Optional[ChemicalAffinityUnit] = Field(
        ChemicalAffinityUnit.joule_per_mole, title="ChemicalAffinityUnit"
    )



class MolarRefractivityUnit(UnitEnum):
    meter_cubed_per_mole = "Item:OSW94bba2ee2f9a573eb5fa99c9331f1626"
    deci_meter_cubed_per_mole = (
        "Item:OSW94bba2ee2f9a573eb5fa99c9331f1626#OSW6eaa02f1d5ad581f97e7e017fab31412"
    )
    centi_meter_cubed_per_mole = (
        "Item:OSW94bba2ee2f9a573eb5fa99c9331f1626#OSW90c99a00002b5483a1ac0638fdbe9078"
    )


class MolarRefractivity(QuantityValue):
    """
    A quantity kind that is a measure of the total polarizability of a mole of substance that depends on the temperature, the index of refraction and the pressure.
    """

    type: Optional[Any] = ["Category:OSWf8e46376106556cfbbf27ebe2af14849"]
    unit: Optional[MolarRefractivityUnit] = Field(
        MolarRefractivityUnit.meter_cubed_per_mole, title="MolarRefractivityUnit"
    )



class LengthMassUnit(UnitEnum):
    kilo_gram_meter = "Item:OSW4a5d124e14e45b8c95bebb544ce245b6"


class LengthMass(QuantityValue):
    """
    This is an autogenerated partial class definition of 'LengthMass'
    """

    type: Optional[Any] = ["Category:OSW4b7dde3787455f5aa84d6783bda3971a"]
    unit: Optional[LengthMassUnit] = Field(
        LengthMassUnit.kilo_gram_meter, title="LengthMassUnit"
    )



class MassAttenuationCoefficientUnit(UnitEnum):
    meter_squared_per_kilo_gram = (
        "Item:OSWd7015166d39d5cae866a40eac3d51896#OSWc811db362efa5d33a49b56ffdd77e54d"
    )


class MassAttenuationCoefficient(QuantityValue):
    """
    "Mass Attenuation Coefficient" is a measurement of how strongly a chemical species or substance absorbs or scatters light at a given wavelength, per unit mass.
    """

    type: Optional[Any] = ["Category:OSW6a7ba5aa1883572e808667e4e0f83ef8"]
    unit: Optional[MassAttenuationCoefficientUnit] = Field(
        MassAttenuationCoefficientUnit.meter_squared_per_kilo_gram,
        title="MassAttenuationCoefficientUnit",
    )



class ForcePerAreaUnit(UnitEnum):
    pascal = "Item:OSWb663e6bff3595e7b93b28fffce66c50c"
    giga_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW49bb4743a5735e189777f3c6bd422a52"
    )
    deca_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW8d40059d9e3951bb97378fe3f119ba21"
    )
    milli_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW38b0e12539b05ce28cd126c8eea29f95"
    )
    mega_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW0ec5bf8132b25e58b7032766bd9b3225"
    )
    kilo_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW264ebdc21f54568593a91bbd832b6fbf"
    )
    hecto_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW482939f123595314beca39ad32d65a15"
    )
    micro_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW5def4be309ce50ee933c99cf4b74e310"
    )


class ForcePerArea(QuantityValue):
    """
    The force applied to a unit area of surface; measured in pascals (SI unit) or in dynes (cgs unit)
    """

    type: Optional[Any] = ["Category:OSW2ff3a26daf13563481acc8b0ebc5b37f"]
    unit: Optional[ForcePerAreaUnit] = Field(
        ForcePerAreaUnit.pascal, title="ForcePerAreaUnit"
    )



class ActivityConcentrationUnit(UnitEnum):
    becquerel_per_meter_cubed = "Item:OSWd3720cbbb37c5c1698a8570b837b5af9"


class ActivityConcentration(QuantityValue):
    """
    The "Activity Concentration", also known as volume activity, and activity density, is .
    """

    type: Optional[Any] = ["Category:OSW815fd9089afe56a99cdf0e0ca0c04543"]
    unit: Optional[ActivityConcentrationUnit] = Field(
        ActivityConcentrationUnit.becquerel_per_meter_cubed,
        title="ActivityConcentrationUnit",
    )



class PowerPerElectricChargeUnit(UnitEnum):
    volt_per_second = "Item:OSW7d0144647c655cbeac604178c20df9c8"
    volt_per_micro_second = (
        "Item:OSW7d0144647c655cbeac604178c20df9c8#OSWa89d207ffc6f502a9f742482fb84c1ad"
    )


class PowerPerElectricCharge(QuantityValue):
    """
    "Power Per Electric Charge" is the amount of energy generated by a unit of electric charge.
    """

    type: Optional[Any] = ["Category:OSW2341adcf1a54557f886137e4180398d9"]
    unit: Optional[PowerPerElectricChargeUnit] = Field(
        PowerPerElectricChargeUnit.volt_per_second, title="PowerPerElectricChargeUnit"
    )



class ThermalResistivityUnit(UnitEnum):
    kelvin_meter_per_watt = "Item:OSWc51652fc56f1518ebabb2c7f7701436e"


class ThermalResistivity(QuantityValue):
    """
    The reciprocal of thermal conductivity is thermal resistivity, measured in $kelvin-metres$ per watt ($K \cdot m/W$).
    """

    type: Optional[Any] = ["Category:OSW22acaaf9b83e5160b8a29b1a4147e848"]
    unit: Optional[ThermalResistivityUnit] = Field(
        ThermalResistivityUnit.kelvin_meter_per_watt, title="ThermalResistivityUnit"
    )



class PhotosyntheticPhotonFluxDensityUnit(UnitEnum):
    mole_per_meter_squared_per_second = "Item:OSW3063bab947d256b1a7a11cdb158d11b1"
    milli_mole_per_meter_squared_per_second = (
        "Item:OSW3063bab947d256b1a7a11cdb158d11b1#OSWd5bf9cdb27765d8bbc553cf3682b1c52"
    )
    micro_mole_per_meter_squared_per_second = (
        "Item:OSW3063bab947d256b1a7a11cdb158d11b1#OSW92a55c5f59b259f8acfe7284e9f7ebe1"
    )


class PhotosyntheticPhotonFluxDensity(QuantityValue):
    """
    Photosynthetically Active Radiation are the wavelengths of light within the visible range of 400 to 700 nanometers (nm) that are critical for photosynthesis. PPFD measures the amount of PAR light (photons) that arrive at the plant’s surface each second. The PPFD is measured at various distances with a Full-spectrum Quantum Sensor, also known as a PAR meter. Natural sunlight has a PAR value of 900-1500μMol/m2/s when the sun is directly overhead. For a grow light to be effective, it should have PAR values of 500-1500 μMol/m2/s.
    """

    type: Optional[Any] = ["Category:OSW930db2af867152fab4e9728fb7f0ae51"]
    unit: Optional[PhotosyntheticPhotonFluxDensityUnit] = Field(
        PhotosyntheticPhotonFluxDensityUnit.mole_per_meter_squared_per_second,
        title="PhotosyntheticPhotonFluxDensityUnit",
    )



class StandardGravitationalParameterUnit(UnitEnum):
    meter_cubed_per_second_squared = "Item:OSW70d2cca5a9c75bec807d755997acbf8c"
    kilo_meter_cubed_per_second_squared = (
        "Item:OSW70d2cca5a9c75bec807d755997acbf8c#OSW111bef40f18158099e03d15fcd4af1fe"
    )


class StandardGravitationalParameter(QuantityValue):
    """
    In celestial mechanics the standard gravitational parameter of a celestial body is the product of the gravitational constant G and the mass M of the body. Expressed as $\mu = G \cdot M$. The SI units of the standard gravitational parameter are $m^{3}s^{-2}$.
    """

    type: Optional[Any] = ["Category:OSW9a1a2b8a06d754dcb2ea44a8cdbd7fd7"]
    unit: Optional[StandardGravitationalParameterUnit] = Field(
        StandardGravitationalParameterUnit.meter_cubed_per_second_squared,
        title="StandardGravitationalParameterUnit",
    )



class ElectricChargeLineDensityUnit(UnitEnum):
    coulomb_per_meter = "Item:OSW375890764ffa5a5cb84e1cbbe16a7315"


class ElectricChargeLineDensity(QuantityValue):
    """
    In electromagnetism, charge density is a measure of electric charge per unit volume of space, in one, two or three dimensions. More specifically: the linear, surface, or volume charge density is the amount of electric charge per unit length, surface area, or volume, respectively. The respective SI units are $C \cdot $, $m^{-1}$, $C \cdot m^{-2}$ or $C \cdot m^{-3}$.
    """

    type: Optional[Any] = ["Category:OSW475a9570e84c5fd886a8b6f889ed24ca"]
    unit: Optional[ElectricChargeLineDensityUnit] = Field(
        ElectricChargeLineDensityUnit.coulomb_per_meter,
        title="ElectricChargeLineDensityUnit",
    )



class VolumePerTimeUnit(UnitEnum):
    meter_cubed_per_second = "Item:OSW4ed5503a56ab514ab3d925287da52a95"
    centi_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSWacda1333cb6958069dc83172f3a047db"
    )
    deci_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSW58c067fb208b5294899599809141c3ff"
    )


class VolumePerTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'VolumePerTime'
    """

    type: Optional[Any] = ["Category:OSW015e42239c0f5ff38b65340955c12f80"]
    unit: Optional[VolumePerTimeUnit] = Field(
        VolumePerTimeUnit.meter_cubed_per_second, title="VolumePerTimeUnit"
    )



class FugacityUnit(UnitEnum):
    pascal = "Item:OSWb663e6bff3595e7b93b28fffce66c50c"
    giga_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW49bb4743a5735e189777f3c6bd422a52"
    )
    deca_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW8d40059d9e3951bb97378fe3f119ba21"
    )
    milli_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW38b0e12539b05ce28cd126c8eea29f95"
    )
    mega_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW0ec5bf8132b25e58b7032766bd9b3225"
    )
    kilo_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW264ebdc21f54568593a91bbd832b6fbf"
    )
    hecto_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW482939f123595314beca39ad32d65a15"
    )
    micro_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW5def4be309ce50ee933c99cf4b74e310"
    )


class Fugacity(QuantityValue):
    """
    "Fugacity" of a real gas is an effective pressure which replaces the true mechanical pressure in accurate chemical equilibrium calculations. It is equal to the pressure of an ideal gas which has the same chemical potential as the real gas.
    """

    type: Optional[Any] = ["Category:OSW8a40f5d0db99505687782d8e905f50d4"]
    unit: Optional[FugacityUnit] = Field(FugacityUnit.pascal, title="FugacityUnit")



class PoyntingVectorUnit(UnitEnum):
    watt_per_meter_squared = "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11"
    watt_per_centi_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWa735be7b016c510f98dd404ee42c6722"
    )
    micro_watt_per_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWbec47ab085945564b8bc080ab7934395"
    )
    milli_watt_per_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWf33a1a99c6055b178a0b973e57e1aacb"
    )
    pico_watt_per_meter_squared = (
        "Item:OSW7f2c167c5a39550d91c1f95cc01a9a11#OSWf194c328c8ef587c823773008774afc8"
    )


class PoyntingVector(QuantityValue):
    """
    "Poynting Vector" is the vector product of the electric field strength $\mathbf{E}$ and the magnetic field strength $\mathbf{H}" of the electromagnetic field at a given point. The flux of the Poynting vector through a closed surface is equal to the electromagnetic power passing through this surface. For a periodic electromagnetic field, the time average of the Poynting vector is a vector of which, with certain reservations, the direction may be considered as being the direction of propagation of electromagnetic energy and the magnitude considered as being the average electromagnetic power flux density.
    """

    type: Optional[Any] = ["Category:OSWa43ea013a5225362ab7233fa2d33a5aa"]
    unit: Optional[PoyntingVectorUnit] = Field(
        PoyntingVectorUnit.watt_per_meter_squared, title="PoyntingVectorUnit"
    )



class SoundReductionIndexUnit(UnitEnum):
    byte = "Item:OSW20ac6724f1a05ee884222d546955e78f"


class SoundReductionIndex(QuantityValue):
    """
    The Sound Reduction Index is used to measure the level of sound insulation provided by a structure such as a wall, window, door, or ventilator.
    """

    type: Optional[Any] = ["Category:OSW39461742983959d797023ac052a90323"]
    unit: Optional[SoundReductionIndexUnit] = Field(
        SoundReductionIndexUnit.byte, title="SoundReductionIndexUnit"
    )



class QuarticElectricDipoleMomentPerCubicEnergyUnit(UnitEnum):
    field_4_per_joule_cubed = "Item:OSWe0b098248f7557aaa6a892a6ecbd32b8"


class QuarticElectricDipoleMomentPerCubicEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'QuarticElectricDipoleMomentPerCubicEnergy'
    """

    type: Optional[Any] = ["Category:OSW2caa3692da12558c97bcfa1841254d1b"]
    unit: Optional[QuarticElectricDipoleMomentPerCubicEnergyUnit] = Field(
        QuarticElectricDipoleMomentPerCubicEnergyUnit.field_4_per_joule_cubed,
        title="QuarticElectricDipoleMomentPerCubicEnergyUnit",
    )



class SoundVolumeVelocityUnit(UnitEnum):
    meter_cubed_per_second = "Item:OSW4ed5503a56ab514ab3d925287da52a95"
    centi_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSWacda1333cb6958069dc83172f3a047db"
    )
    deci_meter_cubed_per_second = (
        "Item:OSW4ed5503a56ab514ab3d925287da52a95#OSW58c067fb208b5294899599809141c3ff"
    )


class SoundVolumeVelocity(QuantityValue):
    """
    Sound Volume Velocity is the product of particle velocity $v$ and the surface area $S$ through which an acoustic wave of frequency $f$ propagates. Also, the surface integral of the normal component of the sound particle velocity over the cross-section (through which the sound propagates). It is used to calculate acoustic impedance.
    """

    type: Optional[Any] = ["Category:OSW4fcfc4adb6be5e7c97a128565fb91932"]
    unit: Optional[SoundVolumeVelocityUnit] = Field(
        SoundVolumeVelocityUnit.meter_cubed_per_second, title="SoundVolumeVelocityUnit"
    )



class LengthMolarEnergyUnit(UnitEnum):
    joule_meter_per_mole = "Item:OSWb4031d8f85595a128c76bdeb7bb1cbd7"


class LengthMolarEnergy(QuantityValue):
    """
    This is an autogenerated partial class definition of 'LengthMolarEnergy'
    """

    type: Optional[Any] = ["Category:OSWcc185b33860b596a82edbb6eae8f7377"]
    unit: Optional[LengthMolarEnergyUnit] = Field(
        LengthMolarEnergyUnit.joule_meter_per_mole, title="LengthMolarEnergyUnit"
    )



class HamiltonFunctionUnit(UnitEnum):
    joule = "Item:OSW730568cd7ae65906abbbcef1d15cb074"
    peta_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW4e7003f5d7ff58a190167711dd63b0bd"
    )
    kilo_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWad2518d42b685f569679c3599455c3d3"
    )
    milli_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW6df751011258508e9d15967190c819f3"
    )
    femto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW2d5cdc08b064506e8f9a5b0456b7a0b3"
    )
    tera_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW0ac3643d930d5c99936e5ece487a9634"
    )
    exa_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW5ba80670b2945c08b35551442d3169d5"
    )
    giga_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc26bf1cf449d56ef8122745336585d2b"
    )
    mega_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc1525b1f1fc05c40b9715328bf707805"
    )
    atto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWa73c696efa58519aa07c265ea965ceda"
    )


class HamiltonFunction(QuantityValue):
    """
    The Hamilton–Jacobi equation (HJE) is a necessary condition describing extremal geometry in generalizations of problems from the calculus of variations.
    """

    type: Optional[Any] = ["Category:OSW8996de349e2f5dedaa85927e1aa63f96"]
    unit: Optional[HamiltonFunctionUnit] = Field(
        HamiltonFunctionUnit.joule, title="HamiltonFunctionUnit"
    )



class CurvatureUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class Curvature(QuantityValue):
    """
    In mathematics "Curvature" is the amount by which a geometric object deviates from being flat, or straight in the case of a line, but this is defined in different ways depending on the context.
    """

    type: Optional[Any] = ["Category:OSW878316f29355549a8eb66a25d812bd9e"]
    unit: Optional[CurvatureUnit] = Field(
        CurvatureUnit.per_meter, title="CurvatureUnit"
    )



class ReactanceUnit(UnitEnum):
    ohm = "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1"
    kilo_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5e05beabf6935ae2b559c1cffc788110"
    )
    milli_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWa8d17cb3f4255320af6052cbd471d716"
    )
    tera_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5196e38637c752e58c2b5be5521e4234"
    )
    giga_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW66dbbd77c6ca5d5684b223fdfcc7b773"
    )
    mega_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW14b14dd3c32d5ee199a67e3796734a4a"
    )
    micro_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWacd4090bd8335717b6eea6b8c1151b29"
    )


class Reactance(QuantityValue):
    """
    "Reactance" is the opposition of a circuit element to a change of electric current or voltage, due to that element's inductance or capacitance. A built-up electric field resists the change of voltage on the element, while a magnetic field resists the change of current. The notion of reactance is similar to electrical resistance, but they differ in several respects. Capacitance and inductance are inherent properties of an element, just like resistance.
    """

    type: Optional[Any] = ["Category:OSW2f8fe69b4fc55c839e551a63b21bcfbf"]
    unit: Optional[ReactanceUnit] = Field(ReactanceUnit.ohm, title="ReactanceUnit")



class MagneticVectorPotentialUnit(UnitEnum):
    second_volt_per_meter = "Item:OSWf63c15f03855534fabdc39bb5403d1ff"


class MagneticVectorPotential(QuantityValue):
    """
    "Magnetic Vector Potential" is the vector potential of the magnetic flux density. The magnetic vector potential is not unique since any irrotational vector field quantity can be added to a given magnetic vector potential without changing its rotation. Under static conditions the magnetic vector potential is often chosen so that its divergence is zero.
    """

    type: Optional[Any] = ["Category:OSW4e658af1bb265ba78eb72669e48708e2"]
    unit: Optional[MagneticVectorPotentialUnit] = Field(
        MagneticVectorPotentialUnit.second_volt_per_meter,
        title="MagneticVectorPotentialUnit",
    )



class SecondAxialMomentOfAreaUnit(UnitEnum):
    field_4 = "Item:OSWe4f01fe00389574e905718a14481ed36"
    field_4_1 = (
        "Item:OSWe4f01fe00389574e905718a14481ed36#OSW73b630d93619585bbc7f4a3a4a3be104"
    )
    field_4_2 = (
        "Item:OSWe4f01fe00389574e905718a14481ed36#OSW568d0d17db6551c1993de3d51c6051cc"
    )


class SecondAxialMomentOfArea(QuantityValue):
    """
    The moment of inertia, also called mass moment of inertia, rotational inertia, polar moment of inertia of mass, or the angular mass is a property of a distribution of mass in space that measures its resistance to rotational acceleration about an axis.
    """

    type: Optional[Any] = ["Category:OSW607a4c4f2b4855899168d36755af9152"]
    unit: Optional[SecondAxialMomentOfAreaUnit] = Field(
        SecondAxialMomentOfAreaUnit.field_4, title="SecondAxialMomentOfAreaUnit"
    )



class LengthUnit(UnitEnum):
    meter = "Item:OSWf101d25e944856e3bd4b4c9863db7de2"
    centi_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSWe55fa0526c5d58c8a166d59ab5455fd9"
    )
    micro_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSWb2830572baec5cca970dde12bf0f5a2a"
    )
    kilo_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSWb1de8f91f1275572b37c2edfe40d5de6"
    )
    hecto_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSW53a491fdba4d52428769e4bd5c447906"
    )
    deci_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSWf89b36f291825b78b2e376b41104ed80"
    )
    nano_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSW60a0f8bd28955fd6ae61177af381696c"
    )
    deca_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSWf488c3090a5c542aa45dd20b7d37a8ec"
    )
    fermi = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSW53d6030c99a152d28ce56e57b5376f95"
    )
    milli_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSW322dec469be75aedb008b3ebff29db86"
    )
    pico_meter = (
        "Item:OSWf101d25e944856e3bd4b4c9863db7de2#OSW419e951a0df45ae8a8a27806200814b7"
    )


class Length(QuantityValue):
    """
    In geometric measurements, length most commonly refers to the est dimension of an object. In some contexts, the term "length" is reserved for a certain dimension of an object along which the length is measured.
    """

    type: Optional[Any] = ["Category:OSWee9c7e5c343e542cb5a8b4648315902f"]
    unit: Optional[LengthUnit] = Field(LengthUnit.meter, title="LengthUnit")



class MassDensityUnit(UnitEnum):
    gram_per_liter = "Item:OSW754b1a3564725113ac583f91ae2ea959"
    milli_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWca4043a385f25aa3a98122f2aefd0d2e"
    )
    micro_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW457d0485a44c57cda788a583bf9ab4ff"
    )
    gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSWe905ceb23b3b550489bed5baa6c9b466"
    )
    kilo_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW40c933269ec45fc1aeef04aefce2b374"
    )
    pico_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW84ec459d4d135bf28a610cd00061d18c"
    )
    milli_gram_per_milli_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW99bbcff947e1508bad38d748ad6ff8e2"
    )
    gram_per_deci_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW1a48aea5dca45c34bbde02b0df02f6f8"
    )
    femto_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW449dc7494f3f5c0bbd9aff1d1fd2f591"
    )
    nano_gram_per_liter = (
        "Item:OSW754b1a3564725113ac583f91ae2ea959#OSW42fdef27c8ae5c8fbf1876c400f27101"
    )


class MassDensity(QuantityValue):
    """
    The mass density or density of a material is its mass per unit volume.
    """

    type: Optional[Any] = ["Category:OSW512cbc54b9a75f4abe8e66c48204ae0f"]
    unit: Optional[MassDensityUnit] = Field(
        MassDensityUnit.gram_per_liter, title="MassDensityUnit"
    )



class HallCoefficientUnit(UnitEnum):
    meter_cubed_per_coulomb = "Item:OSW2f3941ad9ce25c6ba6744243dcc8c352"


class HallCoefficient(QuantityValue):
    """
    "Hall Coefficient" is defined as the ratio of the induced electric field to the product of the current density and the applied magnetic field.
    """

    type: Optional[Any] = ["Category:OSWb0a0f821d413556691eb1027578097ed"]
    unit: Optional[HallCoefficientUnit] = Field(
        HallCoefficientUnit.meter_cubed_per_coulomb, title="HallCoefficientUnit"
    )



class PowerPerAreaQuarticTemperatureUnit(UnitEnum):
    field_4_per_meter_squared = "Item:OSW88f406fb6a1250eab2d89590d6488f19"


class PowerPerAreaQuarticTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'PowerPerAreaQuarticTemperature'
    """

    type: Optional[Any] = ["Category:OSW2455e65da40951d19c3570531c3e3bf1"]
    unit: Optional[PowerPerAreaQuarticTemperatureUnit] = Field(
        PowerPerAreaQuarticTemperatureUnit.field_4_per_meter_squared,
        title="PowerPerAreaQuarticTemperatureUnit",
    )



class AmountOfSubstancePerMassUnit(UnitEnum):
    mole_per_kilo_gram = "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b"
    centi_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW9abfd6b6d96b507abac8057d6e35a74f"
    )
    micro_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSWa9d227b6d12958eba67fdf22b0934535"
    )
    femto_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSWce6b64163d095affbef6daa39c9cd063"
    )
    pico_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSWd77b5543087f560caec2016c89521715"
    )
    milli_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW78a5da75d0d15046935df4e27fa7d3a9"
    )
    nano_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW51bd13e67a4758bba50388bd5cffe504"
    )
    kilo_mole_per_kilo_gram = (
        "Item:OSWfd92e9c2c69754f78e4145ad3d31c34b#OSW84e7943cec52598082a96c43ab77d33a"
    )


class AmountOfSubstancePerMass(QuantityValue):
    """
    This is an autogenerated partial class definition of 'AmountOfSubstancePerMass'
    """

    type: Optional[Any] = ["Category:OSWefff8e22b4d65024bd044362634938e1"]
    unit: Optional[AmountOfSubstancePerMassUnit] = Field(
        AmountOfSubstancePerMassUnit.mole_per_kilo_gram,
        title="AmountOfSubstancePerMassUnit",
    )



class SpecificEnergyUnit(UnitEnum):
    milli_joule_per_gram = (
        "Item:OSW0fb024653eb9557482d93f027840ee33#OSW27784b13f8b75b47875a87f13de1cde9"
    )


class SpecificEnergy(QuantityValue):
    """
    $\textit{Specific Energy}$ is defined as the energy per unit mass.
      Common metric units are $J/kg$.
      It is an intensive property.
      Contrast this with energy, which is an extensive property.
      There are two main types of specific energy: potential energy and specific kinetic energy.
      Others are the $\textit{gray}$ and $\textit{sievert}$, which are measures for the absorption of radiation.
      $$$$
      The concept of specific energy applies to a particular or theoretical way of extracting useful energy from the material considered that is usually implied by context.
      These intensive properties are each symbolized by using the lower case letter of the symbol for the corresponding extensive property,
       which is symbolized by a capital letter.
      For example, the extensive thermodynamic property enthalpy is symbolized by $H$; specific enthalpy is symbolized by $h$.
    """

    type: Optional[Any] = ["Category:OSW9a32b5a84f235a0cb0a9e9fba9bd252e"]
    unit: Optional[SpecificEnergyUnit] = Field(
        SpecificEnergyUnit.milli_joule_per_gram, title="SpecificEnergyUnit"
    )



class DimensionlessUnit(UnitEnum):
    field_ = "Item:OSW5d3fe58ebbac5483bad8904ff8811366"


class Dimensionless(QuantityValue):
    """
    In dimensional analysis, a dimensionless quantity or quantity of dimension one is a quantity without an associated physical dimension. It is thus a "pure" number, and as such always has a dimension of 1. Dimensionless quantities are widely used in mathematics, physics, engineering, economics, and in everyday life (such as in counting). Numerous well-known quantities, such as $\pi$, $\epsilon$, and $\psi$, are dimensionless. By contrast, non-dimensionless quantities are measured in units of length, area, time, etc. Dimensionless quantities are often defined as products or ratios of quantities that are not dimensionless, but whose dimensions cancel out when their powers are multiplied.
    """

    type: Optional[Any] = ["Category:OSWbcaa33bd770e53e09d5e6087d141648b"]
    unit: Optional[DimensionlessUnit] = Field(
        DimensionlessUnit.field_, title="DimensionlessUnit"
    )



class LinearIonizationUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class LinearIonization(QuantityValue):
    """
    "Linear Ionization"  is a description of how the ionization of an atom or molecule takes place. For example, an ion with a +2 charge can be created only from an ion with a +1 charge or a +3 charge. That is, the numerical charge of an atom or molecule must change sequentially, always moving from one number to an adjacent, or sequential, number. Using sequential ionization definition.
    """

    type: Optional[Any] = ["Category:OSW1199859d969959cf9609fefc5c904183"]
    unit: Optional[LinearIonizationUnit] = Field(
        LinearIonizationUnit.per_meter, title="LinearIonizationUnit"
    )



class SpecificHeatPressureUnit(UnitEnum):
    joule_per_kelvin_per_kilo_gram_per_pascal = (
        "Item:OSW85f51fc6962e5c5ea5e541ad1bdce849"
    )


class SpecificHeatPressure(QuantityValue):
    """
    Specific heat at a constant pressure.
    """

    type: Optional[Any] = ["Category:OSWf27c1fdb12955ad2b62450acb52f702f"]
    unit: Optional[SpecificHeatPressureUnit] = Field(
        SpecificHeatPressureUnit.joule_per_kelvin_per_kilo_gram_per_pascal,
        title="SpecificHeatPressureUnit",
    )



class AreaTemperatureUnit(UnitEnum):
    kelvin_meter_squared = "Item:OSWe74a789a7a8c5e499c23e49bd2a6b220"


class AreaTemperature(QuantityValue):
    """
    This is an autogenerated partial class definition of 'AreaTemperature'
    """

    type: Optional[Any] = ["Category:OSW2c27b4cb42c854299931e28ebd6a601b"]
    unit: Optional[AreaTemperatureUnit] = Field(
        AreaTemperatureUnit.kelvin_meter_squared, title="AreaTemperatureUnit"
    )



class ElectrolyticConductivityUnit(UnitEnum):
    siemens_per_meter = "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d"
    pico_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWc9f2986f0974565b904f1d0d756d5318"
    )
    milli_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWd609b57361b3560d8614f22a0031921f"
    )
    nano_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW6cc3591d052d589cb271f6710f816486"
    )
    mega_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW27b6c423e529517ba2d3f466d2c822b4"
    )
    micro_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWa26d6194b3be5f54a4665a01e3df9426"
    )
    siemens_per_centi_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW88703a966490546d89632c3336e28b2a"
    )
    kilo_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSWe2d30b3b09325ef7819f6d51071e147e"
    )
    deci_siemens_per_meter = (
        "Item:OSWd3fc3766e5c05e0cb845b81a590bbd9d#OSW7b2e1f125aa350409a4f5d467534727a"
    )


class ElectrolyticConductivity(QuantityValue):
    """
    "Electrolytic Conductivity" of an electrolyte solution is a measure of its ability to conduct electricity.
    """

    type: Optional[Any] = ["Category:OSW4c8a2aa1efad5db1a05f9ae73ee05fcf"]
    unit: Optional[ElectrolyticConductivityUnit] = Field(
        ElectrolyticConductivityUnit.siemens_per_meter,
        title="ElectrolyticConductivityUnit",
    )



class AccelerationUnit(UnitEnum):
    meter_per_second_squared = "Item:OSWb91fd68d93375855a57c795180c429a3"
    centi_meter_per_second_squared = (
        "Item:OSWb91fd68d93375855a57c795180c429a3#OSW014676a1d72e5f16a59a8d966253ab6f"
    )


class Acceleration(QuantityValue):
    """
    $\textit{Acceleration}$ is the (instantaneous) rate of change of velocity.
      Acceleration may be either linear acceleration, or angular acceleration.
      It is a vector quantity with dimension $length/time^{2}$ for linear acceleration,
       or in the case of angular acceleration, with dimension $angle/time^{2}$.
      $$$$
      In SI units, linear acceleration is measured in $meters/second^{2}$ ($m \cdot s^{-2}$),
       and angular acceleration is measured in $radians/second^{2}$.
      $$$$
      In physics, any increase or decrease in speed is referred to as acceleration and similarly,
       motion in a circle at constant speed is also an acceleration, since the direction component of the velocity is changing.
    """

    type: Optional[Any] = ["Category:OSW347462e67d905995af16f97dc7c9ef48"]
    unit: Optional[AccelerationUnit] = Field(
        AccelerationUnit.meter_per_second_squared, title="AccelerationUnit"
    )



class TemperatureGradientUnit(UnitEnum):
    Celsius_per_meter = "Item:OSWee60f0c86f6051bb9e1c60b77a607ba2"


class TemperatureGradient(QuantityValue):
    """
    The temperature gradient measures the difference of a temperature per length, as for instance used in an external wall or its layers. It is usually measured in K/m.
    """

    type: Optional[Any] = ["Category:OSW6bd60a9ad5185c0db70de4eb4b727073"]
    unit: Optional[TemperatureGradientUnit] = Field(
        TemperatureGradientUnit.Celsius_per_meter, title="TemperatureGradientUnit"
    )



class TotalCurrentDensityUnit(UnitEnum):
    ampere_per_meter_squared = "Item:OSW2b1e97f1edd650c088abbe8896fe0333"
    mega_ampere_per_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWd0a4ce0cc105550b9bcbc416589a1b85"
    )
    kilo_ampere_per_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWa80d9ac2c0455902ab9531512c9b7667"
    )
    ampere_per_milli_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSW8d7d0b57aaba5f8a8f40e8bacc5cb2f6"
    )
    ampere_per_centi_meter_squared = (
        "Item:OSW2b1e97f1edd650c088abbe8896fe0333#OSWec1a540d03745760af1d26077e9d762e"
    )


class TotalCurrentDensity(QuantityValue):
    """
    "Total Current Density" is the sum of the electric current density and the displacement current density.
    """

    type: Optional[Any] = ["Category:OSWcdd31e6abf8253a894c6e44a4282924d"]
    unit: Optional[TotalCurrentDensityUnit] = Field(
        TotalCurrentDensityUnit.ampere_per_meter_squared,
        title="TotalCurrentDensityUnit",
    )



class MolarMassVariationDueToPressureUnit(UnitEnum):
    mole_per_kilo_gram_per_pascal = "Item:OSWe96cbd9b4c9c5e2ab7b4a76d5ad71449"


class MolarMassVariationDueToPressure(QuantityValue):
    """
    The "Variation of Molar Mass" of a gas as a function of pressure.
    """

    type: Optional[Any] = ["Category:OSW6edd0e5986c85950824d854922387dc3"]
    unit: Optional[MolarMassVariationDueToPressureUnit] = Field(
        MolarMassVariationDueToPressureUnit.mole_per_kilo_gram_per_pascal,
        title="MolarMassVariationDueToPressureUnit",
    )



class AdmittanceUnit(UnitEnum):
    siemens = "Item:OSW46249e4c237d546198d98bff0b9d5e93"
    milli_siemens = (
        "Item:OSW46249e4c237d546198d98bff0b9d5e93#OSW8253047fc4835d79b0f31baf3b96182d"
    )
    kilo_siemens = (
        "Item:OSW46249e4c237d546198d98bff0b9d5e93#OSW35746906e9d051c39bdeebdf5736c2ba"
    )
    micro_siemens = (
        "Item:OSW46249e4c237d546198d98bff0b9d5e93#OSWfd5a12b202d2534c9cb0844fb6c4f15e"
    )


class Admittance(QuantityValue):
    """
    "Admittance" is a measure of how easily a circuit or device will allow a current to flow. It is defined as the inverse of the impedance ($Z$).
    """

    type: Optional[Any] = ["Category:OSW6dd896b08fd55c6a9ea1a7270bb59d48"]
    unit: Optional[AdmittanceUnit] = Field(
        AdmittanceUnit.siemens, title="AdmittanceUnit"
    )



class ShearModulusUnit(UnitEnum):
    pascal = "Item:OSWb663e6bff3595e7b93b28fffce66c50c"
    giga_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW49bb4743a5735e189777f3c6bd422a52"
    )
    deca_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW8d40059d9e3951bb97378fe3f119ba21"
    )
    milli_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW38b0e12539b05ce28cd126c8eea29f95"
    )
    mega_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW0ec5bf8132b25e58b7032766bd9b3225"
    )
    kilo_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW264ebdc21f54568593a91bbd832b6fbf"
    )
    hecto_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW482939f123595314beca39ad32d65a15"
    )
    micro_pascal = (
        "Item:OSWb663e6bff3595e7b93b28fffce66c50c#OSW5def4be309ce50ee933c99cf4b74e310"
    )


class ShearModulus(QuantityValue):
    """
    The Shear Modulus or modulus of rigidity, denoted by $G$, or sometimes $S$ or $\mu$, is defined as the ratio of shear stress to the shear strain.
    """

    type: Optional[Any] = ["Category:OSW1aa2d583aaac5af29af356124b0dbc67"]
    unit: Optional[ShearModulusUnit] = Field(
        ShearModulusUnit.pascal, title="ShearModulusUnit"
    )



class ElectricPotentialDifferenceUnit(UnitEnum):
    volt = "Item:OSW85efe1428cb75363a75aab6435e2d98d"
    milli_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW82d25d00b1485cc18c204f95de4536a9"
    )
    micro_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSWc0cb09a94aa553589a59ea70bfccfc96"
    )
    kilo_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW4deed980237a5360b48e0dd1331d4199"
    )
    mega_volt = (
        "Item:OSW85efe1428cb75363a75aab6435e2d98d#OSW78798aa1bdcb57f0aea8d4eb86ff3355"
    )


class ElectricPotentialDifference(QuantityValue):
    """
    "Electric Potential Difference" is a scalar valued quantity associated with an electric field.
    """

    type: Optional[Any] = ["Category:OSW6d9120b2881350c08cd48854acbf1180"]
    unit: Optional[ElectricPotentialDifferenceUnit] = Field(
        ElectricPotentialDifferenceUnit.volt, title="ElectricPotentialDifferenceUnit"
    )



class RadiantIntensityUnit(UnitEnum):
    watt_per_steradian = "Item:OSWeb74cc6d085859178ff708d39709ea29"


class RadiantIntensity(QuantityValue):
    """
    Radiant Intensity is a measure of the intensity of electromagnetic radiation. It is defined as power per unit solid angle.
    """

    type: Optional[Any] = ["Category:OSWe7fa402cf56d511e81727e5f976a1c9f"]
    unit: Optional[RadiantIntensityUnit] = Field(
        RadiantIntensityUnit.watt_per_steradian, title="RadiantIntensityUnit"
    )



class ImpedanceUnit(UnitEnum):
    ohm = "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1"
    kilo_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5e05beabf6935ae2b559c1cffc788110"
    )
    milli_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWa8d17cb3f4255320af6052cbd471d716"
    )
    tera_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW5196e38637c752e58c2b5be5521e4234"
    )
    giga_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW66dbbd77c6ca5d5684b223fdfcc7b773"
    )
    mega_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSW14b14dd3c32d5ee199a67e3796734a4a"
    )
    micro_ohm = (
        "Item:OSWf9a174b6598a52fe8b9ac50ee48bf7a1#OSWacd4090bd8335717b6eea6b8c1151b29"
    )


class Impedance(QuantityValue):
    """
    "Impedance" is the measure of the opposition that a circuit presents to the passage of a current when a voltage is applied. In quantitative terms, it is the complex ratio of the voltage to the current in an alternating current (AC) circuit. Impedance extends the concept of resistance to AC circuits, and possesses both magnitude and phase, unlike resistance, which has only magnitude. When a circuit is driven with direct current (DC), there is no distinction between impedance and resistance; the latter can be thought of as impedance with zero phase angle.
    """

    type: Optional[Any] = ["Category:OSW3e38ca0ea54e5d02917c52434bcf41d6"]
    unit: Optional[ImpedanceUnit] = Field(ImpedanceUnit.ohm, title="ImpedanceUnit")



class FrequencyUnit(UnitEnum):
    hertz = "Item:OSW7496c09c41b154bdba82f6d09195cae5"
    mega_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSWb5d0dd4f66285e15af5977a1b77d5daa"
    )
    kilo_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSWfbbfa62ac8095c5bb37ea9f22ab121dd"
    )
    giga_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSW37c66b2e350050d891107e427a1c0210"
    )
    tera_hertz = (
        "Item:OSW7496c09c41b154bdba82f6d09195cae5#OSW5860049cdfae5d64abcd7bb8ace55540"
    )


class Frequency(QuantityValue):
    """
    "Frequency" is the number of occurrences of a repeating event per unit time. The repetition of the events may be periodic (that is. the length of time between event repetitions is fixed) or aperiodic (i.e. the length of time between event repetitions varies). Therefore, we distinguish between periodic and aperiodic frequencies. In the SI system, periodic frequency is measured in hertz (Hz) or multiples of hertz, while aperiodic frequency is measured in becquerel (Bq).  In spectroscopy, $\nu$ is mostly used. Light passing through different media keeps its frequency, but not its wavelength or wavenumber.
    """

    type: Optional[Any] = ["Category:OSWc543ebb853385a1a9382f57faad6170d"]
    unit: Optional[FrequencyUnit] = Field(FrequencyUnit.hertz, title="FrequencyUnit")



class CombinedNonEvaporativeHeatTransferCoefficient(QuantityValue):
    """
    "Evaporative Heat Transfer Coefficient" is the areic heat transfer coefficient multiplied by the water vapor pressure difference between skind and the environment, and by the exchange area.
    """

    type: Optional[Any] = ["Category:OSWfe778dcecbe858509d42538c1ed9aca8"]
    unit: Optional[CombinedNonEvaporativeHeatTransferCoefficientUnit] = Field(
        CombinedNonEvaporativeHeatTransferCoefficientUnit.watt_per_kelvin_per_meter_squared,
        title="CombinedNonEvaporativeHeatTransferCoefficientUnit",
    )



class ThermalConductanceUnit(UnitEnum):
    watt_per_kelvin = "Item:OSWcd1c26954cdf5421b201b431b289ee94"


class ThermalConductance(QuantityValue):
    """
    This quantity is also called "Heat Transfer Coefficient".
    """

    type: Optional[Any] = ["Category:OSWda38a6d51c385b428998b15f68bd787e"]
    unit: Optional[ThermalConductanceUnit] = Field(
        ThermalConductanceUnit.watt_per_kelvin, title="ThermalConductanceUnit"
    )



class RotationalFrequency(QuantityValue):
    """
    IfcRotationalFrequencyMeasure is a measure of the number of cycles that an item revolves in unit time. Usually measured in cycles/s.
    """

    type: Optional[Any] = ["Category:OSW8a7f583fbe315d928de45968b0a3403b"]
    unit: Optional[RotationalFrequencyUnit] = Field(
        RotationalFrequencyUnit.hertz, title="RotationalFrequencyUnit"
    )



class LuminousExposureUnit(UnitEnum):
    hour_lux = "Item:OSW91dd8f1236fc5d328855ad69ed6ba6c4"


class LuminousExposure(QuantityValue):
    """
    Luminous Exposure is the time-integrated illuminance.
    """

    type: Optional[Any] = ["Category:OSW3e3b614bb90a58aa89b5dcddd0045fe9"]
    unit: Optional[LuminousExposureUnit] = Field(
        LuminousExposureUnit.hour_lux, title="LuminousExposureUnit"
    )



class AreaTimeUnit(UnitEnum):
    centi_meter_squared_minute = "Item:OSWa5c77be3eb415d749ce66c39717fb676"


class AreaTime(QuantityValue):
    """
    This is an autogenerated partial class definition of 'AreaTime'
    """

    type: Optional[Any] = ["Category:OSW990c8c6a812a50a396497a2038885114"]
    unit: Optional[AreaTimeUnit] = Field(
        AreaTimeUnit.centi_meter_squared_minute, title="AreaTimeUnit"
    )



class MassSpecificBiogeochemicalRateUnit(UnitEnum):
    micro_gram_per_day_per_gram = "Item:OSWe362097950ff5522865e835757765c17"


class MassSpecificBiogeochemicalRate(QuantityValue):
    """
    the rate at which a specific chemical element or compound is processed or transformed within an ecosystem, calculated per unit mass of the relevant biological material. Unreduced, SI unit is g * g-1 * s-1
    """

    type: Optional[Any] = ["Category:OSWfde2a0718a7c5aeca1582631aec8f5e1"]
    unit: Optional[MassSpecificBiogeochemicalRateUnit] = Field(
        MassSpecificBiogeochemicalRateUnit.micro_gram_per_day_per_gram,
        title="MassSpecificBiogeochemicalRateUnit",
    )



class UnknownUnit(UnitEnum):
    Celsius_squared_per_second = "Item:OSWf619f81d86235c0c8ec35b106174a40b"


class Unknown(QuantityValue):
    """
    Placeholder value used for reference from units where it is not clear what a given unit is a measure of.
    """

    type: Optional[Any] = ["Category:OSW9c2f3029e3d45f76a070dbc43f58ccee"]
    unit: Optional[UnknownUnit] = Field(
        UnknownUnit.Celsius_squared_per_second, title="UnknownUnit"
    )



class LevelWidthUnit(UnitEnum):
    joule = "Item:OSW730568cd7ae65906abbbcef1d15cb074"
    peta_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW4e7003f5d7ff58a190167711dd63b0bd"
    )
    kilo_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWad2518d42b685f569679c3599455c3d3"
    )
    milli_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW6df751011258508e9d15967190c819f3"
    )
    femto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW2d5cdc08b064506e8f9a5b0456b7a0b3"
    )
    tera_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW0ac3643d930d5c99936e5ece487a9634"
    )
    exa_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSW5ba80670b2945c08b35551442d3169d5"
    )
    giga_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc26bf1cf449d56ef8122745336585d2b"
    )
    mega_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWc1525b1f1fc05c40b9715328bf707805"
    )
    atto_joule = (
        "Item:OSW730568cd7ae65906abbbcef1d15cb074#OSWa73c696efa58519aa07c265ea965ceda"
    )


class LevelWidth(QuantityValue):
    """
    The "Level Width" is the uncertainty in the energy of a quantum-mechanical system having discrete energy levels in a state that is not strictly stationary. The system may be an atom, a molecule, or an atomic nucleus.
    """

    type: Optional[Any] = ["Category:OSW1a16494f861252618604afb4928a7256"]
    unit: Optional[LevelWidthUnit] = Field(LevelWidthUnit.joule, title="LevelWidthUnit")



class ElectricChargePerMassUnit(UnitEnum):
    ampere_meter_squared_per_joule_per_second = (
        "Item:OSW57e1f78efd6a50fd8f2c35ea808d7b86"
    )


class ElectricChargePerMass(QuantityValue):
    """
    "Electric Charge Per Mass" is the charge associated with a specific mass of a substance. In the SI and ISO systems this is $1 kg$.
    """

    type: Optional[Any] = ["Category:OSW27391d33725254a288fefb618be785f7"]
    unit: Optional[ElectricChargePerMassUnit] = Field(
        ElectricChargePerMassUnit.ampere_meter_squared_per_joule_per_second,
        title="ElectricChargePerMassUnit",
    )



class InverseMagneticFluxUnit(UnitEnum):
    per_weber = "Item:OSW47655982de7d5958a051f4f3aa75b62a"


class InverseMagneticFlux(QuantityValue):
    """
    This is an autogenerated partial class definition of 'InverseMagneticFlux'
    """

    type: Optional[Any] = ["Category:OSWec17c4ff58f052d489572a95d9024b78"]
    unit: Optional[InverseMagneticFluxUnit] = Field(
        InverseMagneticFluxUnit.per_weber, title="InverseMagneticFluxUnit"
    )



class MassRatioUnit(UnitEnum):
    field_ = "Item:OSW36c3b3d668515d6ba8fd68089a3a0371"
    pico_gram_per_gram = (
        "Item:OSW36c3b3d668515d6ba8fd68089a3a0371#OSW0e151b869b4358e09c5be62ba332b9e2"
    )
    field__1 = (
        "Item:OSW36c3b3d668515d6ba8fd68089a3a0371#OSWae508fcfb7fb56c78ae5250e13758161"
    )
    milli_gram_per_gram = (
        "Item:OSW36c3b3d668515d6ba8fd68089a3a0371#OSW31fbfb51bd3f59f8ad0721cb4d285ad3"
    )
    micro_gram_per_gram = (
        "Item:OSW36c3b3d668515d6ba8fd68089a3a0371#OSW8b2109351a6e507492cbce6f37661a92"
    )
    gram_per_kilo_gram = (
        "Item:OSW36c3b3d668515d6ba8fd68089a3a0371#OSWddab3ad9ea7357ebbf27de6e6e20405d"
    )


class MassRatio(QuantityValue):
    """
    In aerospace engineering, mass ratio is a measure of the efficiency of a rocket. It describes how much more massive the vehicle is with propellant than without; that is, it is the ratio of the rocket's wet mass (vehicle plus contents plus propellant) to its dry mass (vehicle plus contents)
    """

    type: Optional[Any] = ["Category:OSWfeea42441eab5f6598b36cda1157f75f"]
    unit: Optional[MassRatioUnit] = Field(MassRatioUnit.field_, title="MassRatioUnit")



class AbsorbedDoseRateUnit(UnitEnum):
    gray_per_second = "Item:OSW4cbc32faa6945fea85c32ee675aff008"


class AbsorbedDoseRate(QuantityValue):
    """
    "Absorbed Dose Rate" is the absorbed dose of ionizing radiation imparted at a given location per unit of time (second, minute, hour, or day).
    """

    type: Optional[Any] = ["Category:OSW2a24ce5e8c585426b905fe16c38b632b"]
    unit: Optional[AbsorbedDoseRateUnit] = Field(
        AbsorbedDoseRateUnit.gray_per_second, title="AbsorbedDoseRateUnit"
    )



class MolarConductivityUnit(UnitEnum):
    meter_squared_siemens_per_mole = "Item:OSW646be3968f185e0ab1832d987570b812"


class MolarConductivity(QuantityValue):
    """
    "Molar Conductivity" is the conductivity of an electrolyte solution divided by the molar concentration of the electrolyte, and so measures the efficiency with which a given electrolyte conducts electricity in solution.
    """

    type: Optional[Any] = ["Category:OSW5ea67a27968a5832bd98c38020c4bd6e"]
    unit: Optional[MolarConductivityUnit] = Field(
        MolarConductivityUnit.meter_squared_siemens_per_mole,
        title="MolarConductivityUnit",
    )



class LinearAbsorptionCoefficientUnit(UnitEnum):
    per_meter = "Item:OSW28e75b089e145904998a54f1c4125bf3"
    per_milli_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWe77bc3c1bd7a566eadb55f3b68d351f2"
    )
    per_nano_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWdc9edf9277ed57cdb7a6f218551afa8d"
    )
    per_centi_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW0dcebe41477056aba0e706c148970688"
    )
    per_kilo_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW124eebfb89dc54bc9cc223fd49c40480"
    )
    per_micro_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSW45c24d8b68485accbdd684f05231c74c"
    )
    per_pico_meter = (
        "Item:OSW28e75b089e145904998a54f1c4125bf3#OSWd0475e49e0715ec488fba3fe0fdd9b02"
    )


class LinearAbsorptionCoefficient(QuantityValue):
    """
    The Linear Absorption Coefficient is a quantity that characterizes how easily a material or medium can be penetrated by a beam of light, sound, particles, or other energy or matter.
    """

    type: Optional[Any] = ["Category:OSW5c809cc846485949a513c8bc406e7e70"]
    unit: Optional[LinearAbsorptionCoefficientUnit] = Field(
        LinearAbsorptionCoefficientUnit.per_meter,
        title="LinearAbsorptionCoefficientUnit",
    )



class ThermalConductivityUnit(UnitEnum):
    watt_per_kelvin_per_meter = "Item:OSW2b8517640ac75611a57b26b56bd5124c"


class ThermalConductivity(QuantityValue):
    """
    In physics, thermal conductivity, $k$ (also denoted as $\lambda$), is the property of a material's ability to conduct heat. It appears primarily in Fourier's Law for heat conduction and is the areic heat flow rate divided by temperature gradient.
    """

    type: Optional[Any] = ["Category:OSW60f1d4c90b5d5f15a5c38d7741ba689e"]
    unit: Optional[ThermalConductivityUnit] = Field(
        ThermalConductivityUnit.watt_per_kelvin_per_meter,
        title="ThermalConductivityUnit",
    )



class Spin(AngularMomentum):
    """
    In quantum mechanics and particle physics "Spin" is an intrinsic form of angular momentum carried by elementary particles, composite particles (hadrons), and atomic nuclei.
    """

    type: Optional[Any] = ["Category:OSWff78da3139af553d81d4720b73d306ca"]



class LoudnessLevel(Dimensionless):
    """
    in phon angegebener Wert als Maß für die Stärke der subjektiven Wahrnehmung eines Schallvorgange, der zahlenmäßig dem in dB angegebenen Schalldruckpegel eines Referenzschalls entspricht, der aus einer frontal einfallenden ebenen Welle mit der Frequenz 1000 Hz besteht und als gleich laut wie das Geräusch empfunden wird
    """

    type: Optional[Any] = ["Category:OSW50eb39182e3457889925e653d5a3bd03"]



class MomentOfInertiaInTheZAxis(MomentOfInertia):
    """
    The rotational inertia or resistance to change in direction or speed of rotation about a defined axis.
    """

    type: Optional[Any] = ["Category:OSW4a37b652a9105d73a07fde7077482acb"]



class DimensionlessRatio(Dimensionless):
    """
    This is an autogenerated partial class definition of 'DimensionlessRatio'
    """

    type: Optional[Any] = ["Category:OSW67faac860ed758758aa4484387e5d5c9"]


class StateOfCharge(DimensionlessRatio):
    """
    ""State of Charge",quantifies the remaining capacity available in a battery at a given time and in relation to a given state of ageing.
    """

    type: Optional[Any] = ["Category:OSWd443875dfab1594b91b207cd59e9e0fa"]



class ParticleCurrent(Frequency):
    """
    "Particle Current" can be used to describe the net number of particles passing through a surface in an infinitesimal time interval.
    """

    type: Optional[Any] = ["Category:OSW696c218a30c35d4d8c07a1ecf9f185c7"]



class PlanarForce(ForcePerArea):
    """
    Another name for Force Per Area, used by the Industry Foundation Classes (IFC) standard.
    """

    type: Optional[Any] = ["Category:OSWb2e45bfd826e56a8a0fa4b10962cb733"]



class CrossSection(Area):
    """
    "Cross-section" is used to express the likelihood of interaction between particles. For a specified target particle and for a specified reaction or process produced by incident charged or uncharged particles of specified type and energy, it is the mean number of such reactions or processes divided by the incident-particle fluence.
    """

    type: Optional[Any] = ["Category:OSWa002dbedf44c5a86a375783a4e7ba6e7"]



class Reflectance(DimensionlessRatio):
    """
    Reflectance generally refers to the fraction of incident power that is reflected at an interface, while the term "reflection coefficient" is used for the fraction of electric field reflected. Reflectance is always a real number between zero and 1.0.
    """

    type: Optional[Any] = ["Category:OSWe5e3a7fe15ab5beaa32db082ed17e1d5"]


class Reflectivity(Reflectance):
    """
    For homogeneous and semi-infinite materials, reflectivity is the same as reflectance. Reflectivity is the square of the magnitude of the Fresnel reflection coefficient, which is the ratio of the reflected to incident electric field; as such the reflection coefficient can be expressed as a complex number as determined by the Fresnel equations for a single layer, whereas the reflectance is always a positive real number.

    For layered and finite media, according to the CIE, reflectivity is distinguished from reflectance by the fact that reflectivity is a value that applies to thick reflecting objects. When reflection occurs from thin layers of material, internal reflection effects can cause the reflectance to vary with surface thickness. Reflectivity is the limit value of reflectance as the sample becomes thick; it is the intrinsic reflectance of the surface, hence irrespective of other parameters such as the reflectance of the rear surface. Another way to interpret this is that the reflectance is the fraction of electromagnetic power reflected from a specific sample, while reflectivity is a property of the material itself, which would be measured on a perfect machine if the material filled half of all space.
    """

    type: Optional[Any] = ["Category:OSWcabbcff548045cd4adb4e39bdafa328e"]



class ThermodynamicCriticalMagneticFluxDensity(MagneticFluxDensity):
    """
    "Thermodynamic Critical Magnetic Flux Density" is the maximum magnetic field strength below which a material remains superconducting.
    """

    type: Optional[Any] = ["Category:OSW1f2d386a47e4522e99a01df0d0b4393d"]



class StagePropellantMass(Mass):
    """
    This is an autogenerated partial class definition of 'StagePropellantMass'
    """

    type: Optional[Any] = ["Category:OSWf46572064b585f959008296d2c0d7bda"]



class UpperCriticalMagneticFluxDensity(MagneticFluxDensity):
    """
    "Upper Critical Magnetic Flux Density" for type II superconductors, is the threshold magnetic flux density for disappearance of bulk superconductivity.
    """

    type: Optional[Any] = ["Category:OSWb7c211092f5a57a2978f297e390675e1"]



class CartesianArea(Area):
    """
    "Area" is a quantity that expresses the extent of a two-dimensional surface or shape, or planar lamina, in the plane.
    """

    type: Optional[Any] = ["Category:OSW022058c6b4a3517cb9d5a00efac71e12"]



class EccentricityOfOrbit(DimensionlessRatio):
    """
    The orbital eccentricity of an astronomical object is a parameter that determines the amount by which its orbit around another body deviates from a perfect circle. In a two-body problem with inverse-square-law force, every orbit is a Kepler orbit. The eccentricity of this Kepler orbit is a positive number that defines its shape.
    """

    type: Optional[Any] = ["Category:OSW577e79a6dcff5f1ea297ca5c75e2a4a6"]



class LinearExpansionCoefficient(ExpansionRatio):
    """
    This is an autogenerated partial class definition of 'LinearExpansionCoefficient'
    """

    type: Optional[Any] = ["Category:OSW1f35ae0499035b23a508c8017306a1a8"]



class DiffusionArea(Area):
    """
    "Diffusion Area" in an infinite homogenous medium, is one-sixth of the mean square distance between the point where a neutron enters a specified class and the point where it leaves that class.
    """

    type: Optional[Any] = ["Category:OSW0b80c1b75624573dacff39addc27fd98"]



class MeanFreePath(Length):
    """
    "Mean Free Path" is the average distance travelled by a moving particle (such as an atom, a molecule, a photon) between successive impacts (collisions) which modify its direction or energy or other particle properties.
    """

    type: Optional[Any] = ["Category:OSW79e488804697561c90bd9fe6081b7747"]



class ThermalUtilizationFactorForFission(Dimensionless):
    """
    Probability that a neutron that gets absorbed does so in the fuel material.
    """

    type: Optional[Any] = ["Category:OSW3df9fbff888b55cb91302e604817aa3b"]



class Pressure(ForcePerArea):
    """
    Pressure is an effect which occurs when a force is applied on a surface. Pressure is the amount of force acting on a unit area. Pressure is distinct from stress, as the former is the ratio of the component of force normal to a surface to the surface area. Stress is a tensor that relates the vector force to the vector area.
    """

    type: Optional[Any] = ["Category:OSWb58cb5a4654f52e1804c74c035d21352"]


class VaporPressure(Pressure):
    """
    A pressure that is the one exerted by a substance vapor in thermodynamic equilibrium with either its solid or liquid phase at a given temperature in a closed system.
    """

    type: Optional[Any] = ["Category:OSW0a5491ac7e595f04b5c7efd96b101eb2"]



class FrictionCoefficient(DimensionlessRatio):
    """
    "Friction Coefficient" is the ratio of the force of friction between two bodies and the force pressing them together
    """

    type: Optional[Any] = ["Category:OSW8f66d565d52b52bab7fe2840caf54ffa"]



class Count(Dimensionless):
    """
    "Count" is the value of a count of items.
    """

    type: Optional[Any] = ["Category:OSWb0250d3677f6592f9d4329c8b9d5f8d1"]


class NucleonNumber(Count):
    """
    Number of nucleons in an atomic nucleus.A = Z+N. Nuclides with the same value of A are called isobars.
    """

    type: Optional[Any] = ["Category:OSW5644ec02a8435f74946c883721c162c0"]



class TotalPressure(Pressure):
    """
    The total pressure is the sum of the dynamic and static pressures, that is $P_0 = P + q$.
    """

    type: Optional[Any] = ["Category:OSW0301595d3ef35fcb98b63e87d8b3d34c"]



class SpeedOfLight(Speed):
    """
    The quantity kind $\text{Speed of Light}$ is the speed of electomagnetic waves in a given medium.
    """

    type: Optional[Any] = ["Category:OSWead5dcb16a9a5c259862f31eca41609d"]



class LinearForce(ForcePerLength):
    """
    Another name for Force Per Length, used by the Industry Foundation Classes (IFC) standard.
    """

    type: Optional[Any] = ["Category:OSW07c57bfb44bc521d978ee17c347b3eb4"]



class ResistanceRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'ResistanceRatio'
    """

    type: Optional[Any] = ["Category:OSW1a4104b107005ab9973f79ac86392bdd"]



class AreicChargeDensity(ElectricChargePerArea):
    """
    This is an autogenerated partial class definition of 'AreicChargeDensity'
    """

    type: Optional[Any] = ["Category:OSW634ec6dac47f5f439bd6f64e9243351c"]



class LatticePlaneSpacing(Length):
    """
    "Lattice Plane Spacing" is the distance between successive lattice planes.
    """

    type: Optional[Any] = ["Category:OSW7037954044755f1ebb66ec49748bc781"]



class MomentOfInertiaInTheYAxis(MomentOfInertia):
    """
    The rotational inertia or resistance to change in direction or speed of rotation about a defined axis.
    """

    type: Optional[Any] = ["Category:OSW54513644901155ce82c3161b8ce76cf1"]



class InformationEntropy(Dimensionless):
    """
    Information Entropy is a concept from information theory. It tells how much information there is in an event. In general, the more uncertain or random the event is, the more information it will contain. The concept of information entropy was created by a mathematician. He was named Claude Elwood Shannon. It has applications in many areas, including lossless data compression, statistical inference, cryptography and recently in other disciplines as biology, physics or machine learning.
    """

    type: Optional[Any] = ["Category:OSW9b6dead1d47358a099b73ba6b309597e"]


class ShannonDiversityIndex(InformationEntropy):
    """
    Information entropy applied to a collection of indiviual organisms [of selected species] in a sample area. A measure of biodiversity.
    """

    type: Optional[Any] = ["Category:OSWab8d90e4cf375a00a31a76e87df91860"]



class AtomicAttenuationCoefficient(Area):
    """
    "Atomic Attenuation Coefficient" is a measurement of how strongly a chemical species or substance absorbs or scatters light at a given wavelength, per the number of atoms in the substance.
    """

    type: Optional[Any] = ["Category:OSW81c5fd6490545918af3b53f4d68eae2d"]



class AngularAcceleration(InverseSquareTime):
    """
    Angular acceleration is the rate of change of angular velocity over time. Measurement of the change made in the rate of change of an angle that a spinning object undergoes per unit time. It is a vector quantity.  Also called Rotational acceleration. In SI units, it is measured in radians per second squared ($rad/s^2$), and is usually denoted by the Greek letter alpha.
    """

    type: Optional[Any] = ["Category:OSWc635dd8c8ae65263a6d2b3777f5776bb"]



class ExitPlaneTemperature(Temperature):
    """
    This is an autogenerated partial class definition of 'ExitPlaneTemperature'
    """

    type: Optional[Any] = ["Category:OSW56417a8699945e82ab40ada7d4b44973"]



class RocketAtmosphericTransverseForce(Force):
    """
    Transverse force on rocket due to an atmosphere
    """

    type: Optional[Any] = ["Category:OSW58a8aa9d0dbf5a208fad263db52d2a1b"]



class SoundPower(Power):
    """
    Sound power or acoustic power $P_a$ is a measure of sonic energy $E$ per time $t$ unit. It is measured in watts and can be computed as sound intensity ($I$) times area ($A$).
    """

    type: Optional[Any] = ["Category:OSW499c7be1f79251ba989d017a787d40e3"]



class Angle(DimensionlessRatio):
    """
    The abstract notion of angle. Narrow concepts include plane angle and solid angle. While both plane angle and solid angle are dimensionless, they are actually length/length and area/area respectively.
    """

    type: Optional[Any] = ["Category:OSW2339256af71e5635a541ac7f5a437141"]


class Tilt(Angle):
    """
    The angle between an object's orientation vector relative to a reference frame.
      In the context of architecture, this would refer to the angle between the ground and the face of a surface.
    """

    type: Optional[Any] = ["Category:OSWde7fca6167015b5280b935114fbfc76b"]



class ActivityRelatedByMass(MassicActivity):
    """
    quantitative Angabe der Radioaktivität einer Menge eines Radionuklids in einem bestimmten Energiezustand zu einem gegebenen Zeitpunkt dividiert durch die zugehörige Masse dieser Menge #,#quantitative data of the radioactivity of the amount of a radionuclide in a particular state of energy at a defined point in time, divided by the related mass of this quantity
    """

    type: Optional[Any] = ["Category:OSWcfe97306540e52e5882cbbb336f25e33"]



class TargetBogieMass(Mass):
    """
    An informal mass limit established by a Project Office (at the Element Integrated Product Team (IPT) level or below) to control mass.
    """

    type: Optional[Any] = ["Category:OSWa76d2f3b5b215031a315e3ab651e5c32"]



class SignalStrength(ElectricFieldStrength):
    """
    In telecommunications, particularly in radio, signal strength refers to the magnitude of the electric field at a reference point that is a significant distance from the transmitting antenna. It may also be referred to as received signal level or field strength. Typically, it is expressed in voltage per length or signal power received by a reference antenna. High-powered transmissions, such as those used in broadcasting, are expressed in dB-millivolts per metre (dBmV/m).
    """

    type: Optional[Any] = ["Category:OSW2b4e65f26005511487ca6d47b859e932"]


class RfPowerLevel(SignalStrength):
    """
    Radio-Frequency Power. Power level of electromagnetic waves alternating at the frequency of radio waves (up to 10^10 Hz).
    """

    type: Optional[Any] = ["Category:OSW0eab93f86d9359bcbdfa90d6af162d71"]



class ThermodynamicTemperature(Temperature):
    """
    Thermodynamic temperature is the absolute measure of temperature and is one of the principal parameters of thermodynamics.
    Temperature is a physical property of matter that quantitatively expresses the common notions of hot and cold.
    In thermodynamics, in a system of which the entropy is considered as an independent externally controlled variable, absolute, or thermodynamic temperature is defined as the derivative of the internal energy with respect to the entropy. This is a base quantity in the International System of Quantities, ISQ, on which the International System of Units, SI, is based.
    """

    type: Optional[Any] = ["Category:OSW69b648b4fe1a5607b167a699f899be87"]


class CelsiusTemperature(ThermodynamicTemperature):
    """
    "Celsius Temperature", the thermodynamic temperature T_0, is exactly 0.01 kelvin below the thermodynamic temperature of the triple point of water.
    """

    type: Optional[Any] = ["Category:OSW7f41c3f871b9551cbd4032f756f3fc0d"]



class AreicEnergyFlow(PowerPerArea):
    """
    Leistung in festgelegter Ausbreitungsrichtung durch ein dazu senkrechtes Oberflächenelement, dividiert durch dessen Fläche
    """

    type: Optional[Any] = ["Category:OSW268c0467204b54eaa6306808bdc97f6d"]



class QuantumNumber(Dimensionless):
    """
    The "Quantum Number" describes values of conserved quantities in the dynamics of the quantum system. Perhaps the most peculiar aspect of quantum mechanics is the quantization of observable quantities, since quantum numbers are discrete sets of integers or half-integers.
    """

    type: Optional[Any] = ["Category:OSWa35c06b30b7750c49dd53768ffd9e756"]


class TotalAngularMomentumQuantumNumber(QuantumNumber):
    """
    The "Total Angular Quantum Number" describes the magnitude of total angular momentum $J$, where $j$ refers to a specific particle and $J$ is used for the whole system.
    """

    type: Optional[Any] = ["Category:OSW176905fa65165b4d834f093249932fef"]



class FirstMomentOfArea(Volume):
    """
    The first moment of area is the summation of area times distance to an axis. It is a measure of the distribution of the area of a shape in relationship to an axis.
    """

    type: Optional[Any] = ["Category:OSW0a1c176c39c85b16858e4439af7f4e80"]



class RestMass(Mass):
    """
    The $\textit{Rest Mass}$, the invariant mass, intrinsic mass, proper mass, or (in the case of bound systems or objects observed in their center of momentum frame) simply mass, is a characteristic of the total energy and momentum of an object or a system of objects that is the same in all frames of reference related by Lorentz transformations. The mass of a particle type X (electron, proton or neutron) when that particle is at rest. For an electron: $m_e = 9,109 382 15(45) 10^{-31} kg$, for a proton: $m_p = 1,672 621 637(83) 10^{-27} kg$, for a neutron: $m_n = 1,674 927 211(84) 10^{-27} kg$. Rest mass is often denoted $m_0$.
    """

    type: Optional[Any] = ["Category:OSWcc4866e47ced53dfbb709c97a8752530"]



class GravitationalAttraction(Force):
    """
    The force of attraction between all masses in the universe; especially the attraction of the earth's mass for bodies near its surface; the more remote the body the less the gravity; the gravitation between two bodies is proportional to the product of their masses and inversely proportional to the square of the distance between them.
    """

    type: Optional[Any] = ["Category:OSW2389ed8639535a34968939f5fa9559b2"]



class SingleStageLauncherMassRatio(MassRatio):
    """
    This is an autogenerated partial class definition of 'SingleStageLauncherMassRatio'
    """

    type: Optional[Any] = ["Category:OSW0964da9ef1d95299897148151a660792"]



class ByteDataVolume(Count):
    """
    Anzahl von Daten auf Basis einer Zeichenfolge, die aus je 8 Bit besteht
    """

    type: Optional[Any] = ["Category:OSW0f17958464ad51c68861156e6ba886e8"]



class LandauGinzburgNumber(DimensionlessRatio):
    """
    "Landau-Ginzburg Number", also known as the Ginzburg-Landau parameter, describes the relationship between London penetration depth and coherence length.
    """

    type: Optional[Any] = ["Category:OSW0edc656a4a2e5537819f189398ab6b74"]



class ElectronAffinity(Energy):
    """
    "Electron Affinity" is the energy difference between an electron at rest at infinity and an electron at the lowest level of the conduction band in an insulator or semiconductor. The the amount of energy released when an electron is added to a neutral atom or molecule to form a negative ion.
    """

    type: Optional[Any] = ["Category:OSW56927c77340d5c3e99ad1a180ed6aa81"]



class ElectricPower(Power):
    """
    "Electric Power" is the rate at which electrical energy is transferred by an electric circuit. In the simple case of direct current circuits, electric power can be calculated as the product of the potential difference in the circuit (V) and the amount of current flowing in the circuit (I): $P = VI$, where $P$ is the power, $V$ is the potential difference, and $I$ is the current. However, in general electric power is calculated by taking the integral of the vector cross-product of the electrical and magnetic fields over a specified area.
    """

    type: Optional[Any] = ["Category:OSW06164d3febb95a42add7826696cc5387"]


class InstantaneousPower(ElectricPower):
    """
    For a two-terminal element or a two-terminal circuit with terminals A and B,
       $\textit{Instantaneous Power}$ is the product of the voltage $u_{AB}$ between the terminals and the electric current i in the element or circuit:
      $$p = u_{AB} \cdot i$$
      Where $u_{AB}$ is the line integral of the electric field strength from A to B,
        and where the electric current in the element or circuit is taken positive if its direction is from A to B and negative in the opposite case.
      $$$$
      For an n-terminal circuit, it is the sum of the instantaneous powers relative to the n - 1 pairs of terminals when one of the terminals is chosen as a common terminal for the pairs.
      $$$$
      For a polyphase element, it is the sum of the instantaneous powers in all phase elements of a polyphase element.
      $$$$
      For a polyphase line consisting of m line conductors and one neutral conductor, it is the sum of the m instantaneous powers expressed for each line conductor by the product of the polyphase line-to-neutral voltage and the corresponding line current.
    """

    type: Optional[Any] = ["Category:OSWd1fc5c3fcd5f59e386f401c22d343569"]



class OrbitalRadialDistance(Length):
    """
    This is an autogenerated partial class definition of 'OrbitalRadialDistance'
    """

    type: Optional[Any] = ["Category:OSWbc45768eb1665c18975fae4c802c6e63"]



class StaticFrictionCoefficient(FrictionCoefficient):
    """
    Static friction is friction between two or more solid objects that are not moving relative to each other. For example, static friction can prevent an object from sliding down a sloped surface.
    """

    type: Optional[Any] = ["Category:OSWb5fe51534e9a5618af6aabad45c2cb28"]



class StoichiometricNumber(Dimensionless):
    """
    Chemical reactions, as macroscopic unit operations, consist of simply a very large number of elementary reactions, where a single molecule reacts with another molecule. As the reacting molecules (or moieties) consist of a definite set of atoms in an integer ratio, the ratio between reactants in a complete reaction is also in integer ratio. A reaction may consume more than one molecule, and the "Stoichiometric Number" counts this number, defined as positive for products (added) and negative for reactants (removed).
    """

    type: Optional[Any] = ["Category:OSW2782ed29d6ac5a2c9549091f3159e20f"]



class ExhaustStreamPower(Power):
    """
    This is an autogenerated partial class definition of 'ExhaustStreamPower'
    """

    type: Optional[Any] = ["Category:OSWdab6db7853625c7ea4459c243af7cfbf"]



class EnergyFluenceRate(PowerPerArea):
    """
    "Energy Fluence Rate" can be used to describe the energy fluence delivered per unit time.
    """

    type: Optional[Any] = ["Category:OSWbe37b1c60f235f87b6272138ce574d4f"]



class Friction(Force):
    """
    "Friction" is the force of two surfaces In contact, or the force of a medium acting on a moving object (that is air on an aircraft). When contacting surfaces move relative to each other, the friction between the two objects converts kinetic energy into thermal energy.
    """

    type: Optional[Any] = ["Category:OSW92473183e45854a8bd13de8f0aefff19"]


class StaticFriction(Friction):
    """
    Static friction is friction between two or more solid objects that are not moving relative to each other. For example, static friction can prevent an object from sliding down a sloped surface.
    """

    type: Optional[Any] = ["Category:OSWbae7311ed4445fb5922b5b8470ff235a"]



class SpeedOfSound(Speed):
    """
    The speed of sound is the distance travelled during a unit of time by a sound wave propagating through an elastic medium.
    """

    type: Optional[Any] = ["Category:OSW2fa92a2959c456ac831a219705ad4288"]


class PhaseSpeedOfSound(SpeedOfSound):
    """
    In a dispersive medium sound speed is a function of sound frequency, through the dispersion relation. The spatial and temporal distribution of a propagating disturbance will continually change. Each frequency component propagates at its own Phase Velocity of Sound.
    """

    type: Optional[Any] = ["Category:OSWfb720501803a5bd18a402d9ef0353000"]



class FermiTemperature(Temperature):
    """
    "Fermi Temperature" is the temperature associated with the Fermi energy.
    """

    type: Optional[Any] = ["Category:OSW869c9ca238655776b81a4d9a9576ffa9"]



class AbsoluteTypographicMeasurement(Length):
    """
    This is an autogenerated partial class definition of 'AbsoluteTypographicMeasurement'
    """

    type: Optional[Any] = ["Category:OSWb6919e9f2e94555a8a7d56a7cc3d9c85"]



class ElectricDisplacementField(ElectricChargePerArea):
    """
    This is an autogenerated partial class definition of 'ElectricDisplacementField'
    """

    type: Optional[Any] = ["Category:OSW5a24fd1c3d865b1c9148be921d0fdbed"]



class MassMargin(Mass):
    """
    Requirement minus predicted value. Margin is used as a metric in risk management. Positive margin mitigates the risk of mass increases from requirements maturation and implementation, underestimated predicted system, or subsystem mass.
    """

    type: Optional[Any] = ["Category:OSWab8bedd41632574e87e72ed839ad7893"]



class DiffusionLengthSolidStatePhysics(Length):
    """
    "Solid State Diffusion Length" is the average distance traveled by a particle, such as a minority carrier in a semiconductor
    """

    type: Optional[Any] = ["Category:OSW9a071c3e82af50f6bef80aee14562a5d"]



class TotalAngularMomentum(AngularMomentum):
    """
    "Total Angular Momentum" combines both the spin and orbital angular momentum of all particles and fields. In atomic and nuclear physics, orbital angular momentum is usually denoted by $l$ or $L$ instead of $\Lambda$. The magnitude of $J$ is quantized so that $J^2 = \hbar^2 j(j + 1)$, where $j$ is the total angular momentum quantum number.
    """

    type: Optional[Any] = ["Category:OSWd0b4541d5a41557db575cdca502f1973"]



class EnergyContent(Energy):
    """
    gespeicherte Energiemenge, die physikalisch oder chemisch nutzbar ist
    """

    type: Optional[Any] = ["Category:OSW40402cb3470f5f399e35e20b06ba615b"]



class ReverberationTime(Time):
    """
    Reverberation Time is the time required for reflections of a direct sound to decay by 60 dB below the level of the direct sound.
    """

    type: Optional[Any] = ["Category:OSW594b0155a9f7506a8c7bc45f4822387f"]



class ActiveEnergy(Energy):
    """
    "Active Energy" is the electrical energy transformable into some other form of energy.
    """

    type: Optional[Any] = ["Category:OSW153b6d9b79ec58949fbe97d2058d995c"]



class PropellantMass(Mass):
    """
    This is an autogenerated partial class definition of 'PropellantMass'
    """

    type: Optional[Any] = ["Category:OSW3cca82ea6a345bc79d209236e827ea73"]


class ElectricPropulsionPropellantMass(PropellantMass):
    """
    This is an autogenerated partial class definition of 'ElectricPropulsionPropellantMass'
    """

    type: Optional[Any] = ["Category:OSW7d9cb17eb1c75492a024f50a69b04ffc"]



class MeanLinearRange(Length):
    """
    "Mean Linear Range" is, in a given material, for specified charged particles of a specified energy, the average displacement of the particles before they stop. That is, the mean totl rectified path length travelled by a particle in the course of slowing down to rest (or to some suitable cut-off energy) in a given substance under specified conditions averaged over a group of particles having the same initial energy.
    """

    type: Optional[Any] = ["Category:OSW46e725aca93151bf828d906615b3ce50"]



class CombustionChamberTemperature(ThermodynamicTemperature):
    """
    This is an autogenerated partial class definition of 'CombustionChamberTemperature'
    """

    type: Optional[Any] = ["Category:OSW61a93711a8ed5cf899742f6750b3b13c"]



class ThermalExpansionCoefficient(ExpansionRatio):
    """
    The "Thermal Expansion Coefficient" is a measure of the thermal expansion coefficient of a material, which expresses its elongation (as a ratio) per temperature difference. It is usually measured in 1/K. A positive elongation per (positive) rise of temperature is expressed by a positive value.
    """

    type: Optional[Any] = ["Category:OSW5fa26223beca509896bee33fd38ea86a"]



class FirstStageMassRatio(MassRatio):
    """
    Mass ratio for the first stage of a multistage launcher.
    """

    type: Optional[Any] = ["Category:OSW57cfdf8210f950a49e21eee105f0ebcf"]



class StrainEnergyDensity(EnergyDensity):
    """
    Defined as the 'work done' for a given strain, that is the area under the stress-strain curve after a specified eation. Source(s): http://www.prepol.com/product-range/product-subpages/terminology
    """

    type: Optional[Any] = ["Category:OSW6e6fb826447c5248813f8cad28ef53d7"]



class EnergyLevel(Energy):
    """
    "Energy Level" is the ionization energy for an electron at the Fermi energy in the interior of a substance.
    """

    type: Optional[Any] = ["Category:OSW58b430623bde5ec8b77d2f701f145fc8"]



class MechanicalTension(ForcePerArea):
    """
    an einem Punkt eines Körpers, an dem eine Kraft angreift, welche die Form des Körpers zu verändern sucht, der Grenzwert des Quotienten Kraft durch Fläche einer ebenen Oberfläche um diesen Punkt, wenn deren Abmessungen gegen null gehen
    """

    type: Optional[Any] = ["Category:OSW3643fe8cf7fa5c5588bd6c68b73fc480"]



class Illuminance1(LuminousFluxPerArea):
    """
    Illuminance is the total luminous flux incident on a surface, per unit area. It is a measure of the intensity of the incident light, wavelength-weighted by the luminosity function to correlate with human brightness perception.
    """

    type: Optional[Any] = ["Category:OSW0e767858fc7a5df0a3be780057b78446"]


class Illuminance(Illuminance1):
    """
    Spherical illuminance is equal to quotient of the total luminous flux $\Phi_v$ incident on a small sphere by the cross section area of that sphere.
    """

    type: Optional[Any] = ["Category:OSW80d4e8b7a89e5054ba5a7f10dcb99838"]



class NeutronNumber(Count):
    """
    "Neutron Number", symbol $N$, is the number of neutrons in a nuclide. Nuclides with the same value of $N$ but different values of $Z$ are called isotones. $N - Z$ is called the neutron excess number.
    """

    type: Optional[Any] = ["Category:OSW6bbe0ce574cc56d08a605c6011d82e6c"]



class MolarThermodynamicEnergy(MolarEnergy):
    """
    auf die Stoffmenge bezogene Energie
    """

    type: Optional[Any] = ["Category:OSW51019f1923e25459af8db3083b6002e9"]



class ThermodynamicTemperature(Temperature):
    """
    Thermodynamic temperature is the absolute measure of temperature and is one of the principal parameters of thermodynamics.
    Temperature is a physical property of matter that quantitatively expresses the common notions of hot and cold.
    In thermodynamics, in a system of which the entropy is considered as an independent externally controlled variable, absolute, or thermodynamic temperature is defined as the derivative of the internal energy with respect to the entropy. This is a base quantity in the International System of Quantities, ISQ, on which the International System of Units, SI, is based.
    """

    type: Optional[Any] = ["Category:OSW69b648b4fe1a5607b167a699f899be87"]



class Incidence(Frequency):
    """
    In epidemiology, incidence is a measure of the probability of occurrence of a given medical condition in a population within a specified period of time.
    """

    type: Optional[Any] = ["Category:OSWe8d1194aeb2e5b9f877867eab5c9cae9"]


class IncidenceProportion(Incidence):
    """
    Incidence proportion (also known as cumulative incidence) is the number of new cases within a specified time period divided by the size of the population initially at risk. For example, if a population initially contains 1,000 non-diseased persons and 28 develop a condition over two years of observation, the incidence proportion is 28 cases per 1,000 persons per two years, i.e. 2.8% per two years.
    """

    type: Optional[Any] = ["Category:OSW85b27ba50cfe5c2589ffbf2156c25ad1"]



class BurnTime(Time):
    """
    This is an autogenerated partial class definition of 'BurnTime'
    """

    type: Optional[Any] = ["Category:OSW73108f4dd6b15fe2ad962094480cfc69"]



class ComplexPower(ElectricPower):
    """
    $\textit{Complex Power}$, under sinusoidal conditions,
       is the product of the phasor $\mathbf{U}$ representing the voltage between the terminals of a linear two-terminal element,
       or two-terminal circuit and the complex conjugate of the phasor $I$ representing the electric current in the element or circuit.
    """

    type: Optional[Any] = ["Category:OSW2e156bd3451d56e9aa27d9604de376f1"]



class NeutronDiffusionLength(Length):
    """
    The neutron diffusion length is equivalent to the relaxation length, that is, to the distance, in which the neutron flux decreases by a factor e
    """

    type: Optional[Any] = ["Category:OSW1b09e4248a1252468c8213a883656ffa"]



class AericHeatFlowRate(PowerPerArea):
    """
    Density of heat flow rate.
    """

    type: Optional[Any] = ["Category:OSWe4e4be24a160562a932a1a36bf7fff9d"]



class ChemicalPotential(MolarEnergy):
    """
    "Chemical Potential", also known as partial molar free energy, is a form of potential energy that can be absorbed or released during a chemical reaction.
    """

    type: Optional[Any] = ["Category:OSW7119e1d761815d4facb1dbee71829517"]


class StandardChemicalPotential(ChemicalPotential):
    """
    "Standard Chemical Potential" is the value of the chemical potential at standard conditions
    """

    type: Optional[Any] = ["Category:OSWc4389e232bdd57d982bfc4bed783818e"]



class Kerma(SpecificEnergy):
    """
    "Kerma" is the sum of the initial kinetic energies of all the charged particles liberated by uncharged ionizing radiation (i.e., indirectly ionizing radiation such as photons and neutrons) in a sample of matter, divided by the mass of the sample.
    """

    type: Optional[Any] = ["Category:OSW7ad0e91748bb5eedac17c39491d0626e"]



class NozzleThroatCrossSectionalArea(Area):
    """
    Cross-sectional area of the nozzle at the throat.
    """

    type: Optional[Any] = ["Category:OSWd827a75e0225570ea3a1ac154234dad2"]



class MassOfTheEarth(Mass):
    """
    Earth mass is the unit of mass equal to that of the Earth.  Earth mass is often used to describe masses of rocky terrestrial planets.
    """

    type: Optional[Any] = ["Category:OSW58c3637b7e515ed8b51f7e9dc4ea424f"]



class Thrust(Force):
    """
    Thrust is a reaction force described quantitatively by Newton's Second and Third Laws. When a system expels or accelerates mass in one direction the accelerated mass will cause a proportional but opposite force on that system.
    """

    type: Optional[Any] = ["Category:OSW7bf742d673495bb8bd77d1ea5295b2cd"]


class VacuumThrust(Thrust):
    """
    This is an autogenerated partial class definition of 'VacuumThrust'
    """

    type: Optional[Any] = ["Category:OSWc92f6543cf0b54d0a5082ef1e67267ad"]



class MolarEquivalent(AmountOfSubstance):
    """
    "Molar Equivalent" is the amount of a substance that reacts with (or is equivalent to) an arbitrary amount (typically one mole) of
    another substance in a given chemical reaction.
    """

    type: Optional[Any] = ["Category:OSWf9c536c2ed285ff4827652539e5e0152"]



class LarmorAngularFrequency(AngularFrequency):
    """
    The "Larmor Frequency" describes angular momentum vector precession about the external field axis with an angular frequency.
    """

    type: Optional[Any] = ["Category:OSWa190a51f7ec150b2aea3c45ff0ac32d3"]



class ElectronMeanFreePath(Length):
    """
    "Electron Mean Free Path" is the mean free path of electrons.
    """

    type: Optional[Any] = ["Category:OSWbbae37b2b2db536789acd5fc581286b9"]



class SoundEnergyDensity(EnergyDensity):
    """
    Sound energy density is the time-averaged sound energy in a given volume divided by that volume. The sound energy density or sound density (symbol $E$ or $w$) is an adequate measure to describe the sound field at a given point as a sound energy value.
    """

    type: Optional[Any] = ["Category:OSW62dc17a84c9e546a9139735645505a35"]



class SpinQuantumNumber1(QuantumNumber):
    """
    The "Spin Quantum Number"  describes the spin (intrinsic angular momentum) of the electron within that orbital, and gives the projection of the spin angular momentum S along the specified axis
    """

    type: Optional[Any] = ["Category:OSWda012dbe914456a09af4429dce5dcc49"]


class SpinQuantumNumber(SpinQuantumNumber1):
    """
    The "Spin Quantum Number"  describes the spin (intrinsic angular momentum) of the electron within that orbital, and gives the projection of the spin angular momentum S along the specified axis
    """

    type: Optional[Any] = ["Category:OSWa284957197dc5db1a46e9efca2d2a645"]



class StrainEnergyReleaseRate(EnergyPerArea):
    """
    In fracture mechanics, the energy release rate, G, is the rate at which energy is transformed as a material undergoes fracture. Mathematically, the energy release rate is expressed as the decrease in total potential energy per increase in fracture surface area, and is thus expressed in terms of energy per unit area.
    """

    type: Optional[Any] = ["Category:OSW00432537c21f566792bfeea72ed63b6f"]



class MacroscopicCrossSection(CrossSection):
    """
    "Macroscopic Cross-section" is the sum of the cross-sections for a reaction or process of a specified type over all atoms or other entities in a given 3D domain, divided by the volume of that domain.
    """

    type: Optional[Any] = ["Category:OSW7825b2bbb4c258348224e4e6d4f364e8"]



class ExitPlaneCrossSectionalArea(Area):
    """
    Cross-sectional area at exit plane of nozzle
    """

    type: Optional[Any] = ["Category:OSW2c615dd1ae0c5b73b77aaeb99c960a6e"]



class HeadEndPressure(Pressure):
    """
    This is an autogenerated partial class definition of 'HeadEndPressure'
    """

    type: Optional[Any] = ["Category:OSW31cf0c812f335d06a0fab1a15b46d6e5"]


class AverageHeadEndPressure(HeadEndPressure):
    """
    This is an autogenerated partial class definition of 'AverageHeadEndPressure'
    """

    type: Optional[Any] = ["Category:OSWe0ed059cb2015747bde44a56c85b8be8"]



class FlashPointTemperature(Temperature):
    """
    A temperature that is the lowest one at which the vapors of a volatile material will ignite if exposed to an ignition source.  It is frequently used to characterize fire hazards and distinguish different flammable fuels.
    """

    type: Optional[Any] = ["Category:OSWaf03e645fd23505eaa56a8201aed7c36"]



class OpeningRatio(DimensionlessRatio):
    """
    In the context of mechanical systems, "opening ratio" might refer to the proportion of time
      or the extent to which a valve or gate is open relative to its maximum capacity.
    """

    type: Optional[Any] = ["Category:OSW713e8c96687f5714a3064fc857b33456"]



class MassOfElectricalPowerSupply(Mass):
    """
    This is an autogenerated partial class definition of 'MassOfElectricalPowerSupply'
    """

    type: Optional[Any] = ["Category:OSWdbbc6a4fe07057ac8135afb96caaf32d"]



class ElectricCurrentPerLength(LinearElectricCurrentDensity):
    """
    This is an autogenerated partial class definition of 'ElectricCurrentPerLength'
    """

    type: Optional[Any] = ["Category:OSW8ba7ac8b06c453e2885cc41c9d9ee0bb"]


class MagneticFieldStrength(ElectricCurrentPerLength):
    """
    $\textit{Magnetic Field Strength}$ is a vector quantity obtained at a given point by subtracting the magnetization $M$ from the magnetic flux density $B$ divided by the magnetic constant $\mu_0$. The magnetic field strength is related to the total current density $J_{tot}$ via: $\text{rot} H = J_{tot}$.
    """

    type: Optional[Any] = ["Category:OSW5066212adfda5519af307363bd1c5c79"]


class AuxillaryMagneticField(MagneticFieldStrength):
    """
    Magnetic Fields surround magnetic materials and electric currents and are detected by the force they exert on other magnetic materials and moving electric charges. The electric and magnetic fields are two interrelated aspects of a single object, called the electromagnetic field. A pure electric field in one reference frame is observed as a combination of both an electric field and a magnetic field in a moving reference frame. The Auxillary Magnetic Field, H characterizes how the true Magnetic Field B influences the organization of magnetic dipoles in a given medium.
    """

    type: Optional[Any] = ["Category:OSW083bc85446db574690adc35135516c66"]



class RankineTemperature(ThermodynamicTemperature):
    """
    Größe, die eine Temperaturskala benutzt, die wie die Kelvin-Skala beim absoluten Temperatur-Nullpunkt (0 K) ihren Nullwert hat, jedoch im Gegensatz zu dieser den Skalenabstand der Fahrenheit-Skala verwendet
    """

    type: Optional[Any] = ["Category:OSW1c1be0134d4e55e2917c5ee4c4adaa39"]



class MassEquivalent(Mass):
    """
    "Mass Equivalent" is the mass of a substance that reacts with (or is equivalent to) an arbitrary mass of
    another substance in a given chemical reaction.
    """

    type: Optional[Any] = ["Category:OSWea12214400965c818daf0b53062ccf4a"]



class ElectronMobility(Mobility):
    """
    This is an autogenerated partial class definition of 'ElectronMobility'
    """

    type: Optional[Any] = ["Category:OSWab83a0c29273584bb4267cdde76fb928"]



class Depth(Length):
    """
    Depth typically refers to the vertical measure of length from the surface of a liquid.
    """

    type: Optional[Any] = ["Category:OSW9c887dd0f7e05d67baab92a2ba4be3bc"]



class OverRangeDistance(Length):
    """
    Additional distance traveled by a rocket because Of excessive initial velocity.
    """

    type: Optional[Any] = ["Category:OSW2bfac452578d5a63a9f56d0ce3c538e0"]



class ControlMass(Mass):
    """
    The upper design gross mass limit of a system at a specified mission event against which margins are calculated after accounting for basic masses of flight hardware, MGA, and uncertainties. It may include propellants, crew, and cargo.
    """

    type: Optional[Any] = ["Category:OSWd6fcda469e6956fcab3790181555ecce"]



class PolarizationField(ElectricChargePerArea):
    """
    The Polarization Field is the vector field that expresses the density of permanent or induced electric dipole moments in a dielectric material. The polarization vector P is defined as the ratio of electric dipole moment per unit volume.
    """

    type: Optional[Any] = ["Category:OSW8c90f5f9c23e50fdb6406d6a819289cc"]



class AverageVacuumThrust(VacuumThrust):
    """
    This is an autogenerated partial class definition of 'AverageVacuumThrust'
    """

    type: Optional[Any] = ["Category:OSWb1a42fde02475c6db7d2b8121feed666"]



class SoundIntensity(PowerPerArea):
    """
    Sound intensity or acoustic intensity ($I$) is defined as the sound power $P_a$ per unit area $A$. The usual context is the noise measurement of sound intensity in the air at a listener's location as a sound energy quantity.
    """

    type: Optional[Any] = ["Category:OSW7450be7f3aa3552e9da4bb8a6d952f9f"]


class TimeAveragedSoundIntensity(SoundIntensity):
    """
    Sound intensity or acoustic intensity ($I$) is defined as the sound power $P_a$ per unit area $A$. The usual context is the noise measurement of sound intensity in the air at a listener's location as a sound energy quantity.
    """

    type: Optional[Any] = ["Category:OSWba1d28c2642f5d28bd675412004bfc15"]



class BraggAngle(Angle):
    """
    "Bragg Angle" describes the condition for a plane wave to be diffracted from a family of lattice planes, the angle between the wavevector of the incident plane wave, and the lattice planes.
    """

    type: Optional[Any] = ["Category:OSW9a7f3c028f7b5055a03fef1d0ec722ee"]



class SpeedRatio(DimensionlessRatio):
    """
    Speed ratio generally refers to the ratio of the rotational speeds of two interconnected rotating components, but it sometimes relates linear speeds.
    """

    type: Optional[Any] = ["Category:OSWdb19a2fd40ed5dc9a32298deac1650e3"]



class InternalEnergy(Energy):
    """
    "Internal Energy" is simply its energy. "internal" refers to the fact that some energy contributions are not considered. For instance, when the total system is in uniform motion, it has kinetic energy. This overall kinetic energy is never seen as part of the internal energy; one could call it external energy. Or, if the system is at constant non-zero height above the surface the Earth, it has constant potential energy in the gravitational field of the Earth. Gravitational energy is only taken into account when it plays a role in the phenomenon of interest, for instance in a colloidal suspension, where the gravitation influences the up- downward motion of the small particles comprising the colloid. In all other cases, gravitational energy is assumed not to contribute to the internal energy; one may call it again external energy.
    """

    type: Optional[Any] = ["Category:OSW774f88c44dcc50cb8bc8b1defc410724"]



class SoundParticleVelocity(Velocity):
    """
    Sound Particle velocity is the velocity v of a particle (real or imagined) in a medium as it transmits a wave. In many cases this is a longitudinal wave of pressure as with sound, but it can also be a transverse wave as with the vibration of a taut string. When applied to a sound wave through a medium of a fluid like air, particle velocity would be the physical speed of a parcel of fluid as it moves back and forth in the direction the sound wave is travelling as it passes.
    """

    type: Optional[Any] = ["Category:OSW2105d9d70ddc5d3597dae2c14da9e3e2"]



class SpecificEnthalpy(SpecificEnergy):
    """
    $\textit{Specific Enthalpy}$ is enthalpy per mass of substance involved. Specific enthalpy is denoted by a lower case h, with dimension of energy per mass (SI unit: joule/kg). In thermodynamics, $\textit{enthalpy}$ is the sum of the internal energy U and the product of pressure p and volume V of a system: $H = U + pV$.  The internal energy U and the work term pV have dimension of energy, in SI units this is joule; the extensive (linear in size) quantity H has the same dimension.
    """

    type: Optional[Any] = ["Category:OSW405e3d0a77f550a7bf632bb907ae9c47"]



class LinearElectricCurrent(LinearElectricCurrentDensity):
    """
    "Linear Electric Linear Current" is the electric current per unit line.
    """

    type: Optional[Any] = ["Category:OSW53042a34f31b52b8a49926a2368d0e12"]


class Magnetization(LinearElectricCurrent):
    """
    "Magnetization" is defined as the ratio of magnetic moment per unit volume. It is a vector-valued quantity.
    """

    type: Optional[Any] = ["Category:OSW6657e0d5f5525ae2b465f952260b5c3e"]



class DensityInCombustionChamber(MassDensity):
    """
    This is an autogenerated partial class definition of 'DensityInCombustionChamber'
    """

    type: Optional[Any] = ["Category:OSW6837c50be0b85f76835e5fdd56bf054f"]



class BurgersVector(Length):
    """
    "Burgers Vector" is the vector characterizing a dislocation, i.e. the closing vector in a Burgers circuit encircling a dislocation line.
    """

    type: Optional[Any] = ["Category:OSW2aeb29e20464500c8df979d1625f6e75"]



class SoundParticleAcceleration(Acceleration):
    """
    In a compressible sound transmission medium - mainly air - air particles get an accelerated motion: the particle acceleration or sound acceleration with the symbol a in $m/s2$. In acoustics or physics, acceleration (symbol: $a$) is defined as the rate of change (or time derivative) of velocity.
    """

    type: Optional[Any] = ["Category:OSWf360ae368617543faa1e4b2205078443"]



class MaximumOperatingPressure(Pressure):
    """
    This is an autogenerated partial class definition of 'MaximumOperatingPressure'
    """

    type: Optional[Any] = ["Category:OSW817c053c46465665a4ba40e2cffd27fb"]



class Radius(Length):
    """
    In classical geometry, the "Radius" of a circle or sphere is any line segment from its center to its perimeter the radius of a circle or sphere is the length of any such segment.
    """

    type: Optional[Any] = ["Category:OSW57a45884de6052698141a5cbe4aaa4ac"]


class ApogeeRadius(Radius):
    """
    Apogee radius of an elliptical orbit
    """

    type: Optional[Any] = ["Category:OSWabce00a019675e0d98ef7b6a5bb573b0"]



class DebyeAngularWavenumber(InverseLength):
    """
    "Debye Angular Wavenumber" is the cut-off angular wavenumber in the Debye model of the vibrational spectrum of a solid.
    """

    type: Optional[Any] = ["Category:OSW3d79fbc6be93589e9e7164f80e6d9e61"]



class EnergyImparted(Energy):
    """
    The "Energy Imparted", is a physical quantity associated with the energy delivered to a particular volume of matter by all the directly and indirectly ionizing particles (i.e. charged and uncharged) entering that volume.
    """

    type: Optional[Any] = ["Category:OSWa4ca419972bd586e9ab6c19db17d04d9"]



class MassFluxDensity(MassPerAreaTime):
    """
    Produkt aus Strömungsgeschwindigkeit und Dichte
    """

    type: Optional[Any] = ["Category:OSWb20394031e71582e963e4a89b43289e7"]



class FahrenheitTemperature(Temperature):
    """
    Größe, deren Nullpunkt durch die Mischungstemperatur von Eis, Wasser und Salmiak (Ammoniumchlorid) definiert ist (-17,8 °C) und deren Fixpunkte auf der Fahrenheit-Skala 32 °F (Schmelztemperatur von Eis) und 212 °F (Siedetemperatur des Wassers) sind
    """

    type: Optional[Any] = ["Category:OSWab84f18a6ca85e0ab17c23c701c650b3"]



class VehicleVelocity(Velocity):
    """
    This is an autogenerated partial class definition of 'VehicleVelocity'
    """

    type: Optional[Any] = ["Category:OSW42543b13af4c5af88462e7ac8ff8707d"]


class EarthClosestApproachVehicleVelocity(VehicleVelocity):
    """
    This is an autogenerated partial class definition of 'EarthClosestApproachVehicleVelocity'
    """

    type: Optional[Any] = ["Category:OSWa4fc82b5131a5f5485b1cee34bb708ab"]



class PayloadMass(Mass):
    """
    Payload mass is the mass of the payload carried by the craft. In a multistage spacecraft the payload mass of the last stage is the mass of the payload and the payload masses of the other stages are considered to be the gross masses of the next stages.
    """

    type: Optional[Any] = ["Category:OSW159c2d66d13552c494a94a5e544de0a6"]



class DragCoefficient(Dimensionless):
    """
    In fluid dynamics, the drag coefficient is a dimensionless quantity that is used to quantify the drag or resistance of an object in a fluid environment such as air or water.
    """

    type: Optional[Any] = ["Category:OSW48ab89ca051756ab9caeadfb5c2cce08"]



class IonCurrent(ElectricCurrent):
    """
    An ion current is the influx and/or efflux of ions through an ion channel.
    """

    type: Optional[Any] = ["Category:OSW03fe5609198b578db061a3dbdf3c720b"]



class AreicMass(MassPerArea):
    """
    Masse dividiert durch die zugehörige Fläche
    """

    type: Optional[Any] = ["Category:OSW89ba427c9d835122b4f19b10afa15f89"]



class CompoundPlaneAngle(PlaneAngle):
    """
    A "Compound Plane Angle" is a compound measure of plane angle in degrees, minutes, seconds, and optionally millionth-seconds of arc.
    """

    type: Optional[Any] = ["Category:OSW116611f951695317bee0d3df1d1796be"]



class SpatialSummationFunction(Length):
    """
    "Spatial Summation Function" is he ability to produce a composite signal from the signals coming into the eyes from different directions.
    """

    type: Optional[Any] = ["Category:OSWf00faa773bc55f9fb027a0986bf4028f"]



class GibbsEnergy(Energy):
    """
    Gibbs Energy is one of the potentials used to measure energy changes in systems as they evolve from an initial state to a final state. The potential used depends on the constraints of the system, such as constant temperature or pressure. $\textit{Internal Energy} is the internal energy of the system, Enthalpy is the internal energy of the system plus the energy related to pressure-volume work, and Helmholtz and Gibbs free energy are the energies available in a system to do useful work when the temperature and volume or the pressure and temperature are fixed, respectively. The name Gibbs Free Energy is also used.
    """

    type: Optional[Any] = ["Category:OSWa8247c6152ee517485f1711f5e5f38b7"]



class BevelGearPitchAngle(Angle):
    """
    Pitch angle in bevel gears is the angle between an element of a pitch cone and its axis. In external and internal bevel gears, the pitch angles are respectively less than and greater than 90 degrees.
    """

    type: Optional[Any] = ["Category:OSWe587d4f03c135c9690c7617187b9055d"]



class VisibleRadiantEnergy(Energy):
    """
    "Visible Radiant Energy", also known as luminous energy, is the energy of electromagnetic waves. It is energy of the particles that are emitted, transferred, or received as radiation.
    """

    type: Optional[Any] = ["Category:OSWfec7990b044c5e3a829891756b36c3a2"]



class Work(Energy):
    """
    A force is said to do Work when it acts on a body so that there is a displacement of the point of application, however small, in the direction of the force.  The concepts of work and energy are closely tied to the concept of force because an applied force can do work on an object and cause a change in energy. Energy is defined as the ability to do work. Work is done on an object when an applied force moves it through a distance. Kinetic energy is the energy of an object in motion. The net work is equal to the change in kinetic energy.
    """

    type: Optional[Any] = ["Category:OSW1be0e0616fe45f6e9acb6395577080b5"]



class PayloadRatio(DimensionlessRatio):
    """
    The payload ratio is defined as the mass of the payload divided by the empty mass of the structure. Because of the extra cost involved in staging rockets, given the choice, it's often more economic to use few stages with a small payload ratio rather than more stages each with a high payload ratio.
    """

    type: Optional[Any] = ["Category:OSW462f63d99aeb52d5b6add6f57653ab66"]



class PressureBurningRateIndex(Dimensionless):
    """
    This is an autogenerated partial class definition of 'PressureBurningRateIndex'
    """

    type: Optional[Any] = ["Category:OSW2ba24c911c375c43a823fe91a4fc825a"]



class MaxOperatingThrust(Thrust):
    """
    This is an autogenerated partial class definition of 'MaxOperatingThrust'
    """

    type: Optional[Any] = ["Category:OSWb9eb9b070fb3584cb6df0d0dda581fb6"]



class Population(Count):
    """
    Population typically refers to the number of people in a single area, whether it be a city or town, region, country, continent, or the world, but can also represent the number of any kind of entity.
    """

    type: Optional[Any] = ["Category:OSW2d1d1f04bf8d579180ad371211ea8969"]



class ElectricPower(Power):
    """
    "Electric Power" is the rate at which electrical energy is transferred by an electric circuit. In the simple case of direct current circuits, electric power can be calculated as the product of the potential difference in the circuit (V) and the amount of current flowing in the circuit (I): $P = VI$, where $P$ is the power, $V$ is the potential difference, and $I$ is the current. However, in general electric power is calculated by taking the integral of the vector cross-product of the electrical and magnetic fields over a specified area.
    """

    type: Optional[Any] = ["Category:OSW06164d3febb95a42add7826696cc5387"]



class CurieTemperature(Temperature):
    """
    "Curie Temperature" is the critical thermodynamic temperature of a ferromagnet.
    """

    type: Optional[Any] = ["Category:OSW0b0a36330fb35c46b17979e278ed3242"]



class Adaptation(Time):
    """
    "Adaptation" is the recovery of visual ability following exposure to light (dark adaptation).
    """

    type: Optional[Any] = ["Category:OSW83d957cf054d539c9ed2a830d7563441"]



class GroupSpeedOfSound(SpeedOfSound):
    """
    In a dispersive medium sound speed is a function of sound frequency, through the dispersion relation. The spatial and temporal distribution of a propagating disturbance will continually change. The group speed of sound describes the propagation of the disturbance.
    """

    type: Optional[Any] = ["Category:OSW5dc3dc74fcb851e49e95b82204c2f2dd"]



class RadiantEnergy(Energy):
    """
    In radiometry,"Radiant Energy} is the energy of electromagnetic waves. The quantity of radiant energy may be calculated by integrating radiant flux (or power) with respect to time.  In nuclear physics, $\textit{Radiant Energy" is energy, excluding rest energy, of the particles that are emitted, transferred, or received.
    """

    type: Optional[Any] = ["Category:OSWf27fad2a3c155c80a21965b7ddc00016"]



class SpeedOfSound(Speed):
    """
    The speed of sound is the distance travelled during a unit of time by a sound wave propagating through an elastic medium.
    """

    type: Optional[Any] = ["Category:OSW2fa92a2959c456ac831a219705ad4288"]



class Wavelength(Length):
    """
    For a monochromatic wave, "wavelength" is the distance between two successive points in a direction perpendicular to the wavefront where at a given instant the phase differs by $2\pi$. The wavelength of a sinusoidal wave is the spatial period of the wave—the distance over which the wave's shape repeats. The SI unit of wavelength is the meter.
    """

    type: Optional[Any] = ["Category:OSW63b3e955e2ee540b834525f44672012d"]



class OlfactoryThreshold(Concentration):
    """
    "Olfactory Threshold" are thresholds for the concentrations of various classes of smell that can be detected.
    """

    type: Optional[Any] = ["Category:OSWc666cb2a4a3656f191ca980983cfe6a8"]



class NozzleThroatDiameter(Length):
    """
    This is an autogenerated partial class definition of 'NozzleThroatDiameter'
    """

    type: Optional[Any] = ["Category:OSW02b07b5b2f095f45afb5157bce27379a"]



class PressureBurningRateConstant(Dimensionless):
    """
    This is an autogenerated partial class definition of 'PressureBurningRateConstant'
    """

    type: Optional[Any] = ["Category:OSW8383080425d3579eade2a3ffc9db4d21"]



class AbsoluteActivity(InverseVolume):
    """
    The "Absolute Activity" is the exponential of the ratio of the chemical potential to $RT$ where $R$ is the gas constant and $T$ the thermodynamic temperature.
    """

    type: Optional[Any] = ["Category:OSW21ccd41585d45a7f97e68ffe96373f47"]



class EquivalentConcentration(Concentration):
    """
    The amount of a substance that reacts with (or is equivalent to) an arbitrary amount (typically one mole) of another substance in a given chemical reaction, per volume.
    """

    type: Optional[Any] = ["Category:OSW1634701efb425f1d8f32fe9ae216cef8"]



class RestEnergy(Energy):
    """
    "Rest Energy" is the energy equivalent of the rest mass of a body, equal to the rest mass multiplied by the speed of light squared.
    """

    type: Optional[Any] = ["Category:OSW4390b2199b2b5c6eaaad67c7eb19a89a"]



class NozzleWallsThrustReaction(Force):
    """
    This is an autogenerated partial class definition of 'NozzleWallsThrustReaction'
    """

    type: Optional[Any] = ["Category:OSW1d953cfeca67574dadd6a6f0c42d7483"]



class LinearForce(ForcePerLength):
    """
    Stiffness is the extent to which an object resists deformation in response to an applied force. Linear Stiffness is the term used in the Industry Foundation Classes (IFC) standard.
    """

    type: Optional[Any] = ["Category:OSW0459ceb071255f8c8bba85be19091874"]



class SpecificImpulseByMass(Velocity):
    """
    This is an autogenerated partial class definition of 'SpecificImpulseByMass'
    """

    type: Optional[Any] = ["Category:OSW50d86e510c6f5ba8982493f58e0ed602"]



class NozzleThroatPressure(Pressure):
    """
    This is an autogenerated partial class definition of 'NozzleThroatPressure'
    """

    type: Optional[Any] = ["Category:OSW6ea9da91798954daa6d0059bfba4ddbe"]



class PhaseDifference(Angle):
    """
    "Phase Difference" is the difference, expressed in electrical degrees or time, between two waves having the same frequency and referenced to the same point in time. Two oscillators that have the same frequency and different phases have a phase difference, and the oscillators are said to be out of phase with each other. The amount by which such oscillators are out of step with each other can be expressed in degrees from $0^\circ$ to $360^\circ$, or in radians from 0 to ${2\pi}$. If the phase difference is $180^\circ$ ($\pi$ radians), then the two oscillators are said to be in antiphase.
    """

    type: Optional[Any] = ["Category:OSW4d94267d704a581cb3c301ab2aab5aa6"]



class ElectricDisplacement(ElectricChargePerArea):
    """
    In a dielectric material the presence of an electric field E causes the bound charges in the material (atomic nuclei and their electrons) to slightly separate, inducing a local electric dipole moment. The Electric Displacement Field, $D$, is a vector field that accounts for the effects of free charges within such dielectric materials. This describes also the charge density on an extended surface that could be causing the field.
    """

    type: Optional[Any] = ["Category:OSW9d0277a494b25238a583c550230d3d0a"]



class PropellantTemperature(Temperature):
    """
    This is an autogenerated partial class definition of 'PropellantTemperature'
    """

    type: Optional[Any] = ["Category:OSWa78a937a78d65bf89d04af65b0ae5b4a"]


class PropellantMeanBulkTemperature(PropellantTemperature):
    """
    This is an autogenerated partial class definition of 'PropellantMeanBulkTemperature'
    """

    type: Optional[Any] = ["Category:OSWdf6291d2dc5253ffb3144631f058ff18"]



class InitialVelocity(Velocity):
    """
    The velocity of a moving body at starting; especially, the velocity of a projectile as it leaves the mouth of a firearm from which it is discharged.
    """

    type: Optional[Any] = ["Category:OSW10412babccf8564e8480aa8965f19f56"]



class SourceVoltageBetweenSubstances(Voltage):
    """
    "Source Voltage Between Substances" is the source voltage between substance a and b.
    """

    type: Optional[Any] = ["Category:OSWd7b24106d1b45f85ba412191d65d7c1d"]



class LarmorAngularFrequency(AngularFrequency):
    """
    The "Cyclotron Angular Frequency" describes angular momentum vector precession about the external field axis with an angular frequency.
    """

    type: Optional[Any] = ["Category:OSW5ff27cfddf435372a70be4040f61d68b"]



class SystolicBloodPressure(Pressure):
    """
    The pressure of blood in the arteries which rises to a maximum as blood is pumped out by the left ventricle (systole) and drops to a minimum in diastole. The systolic/diastolic pressure is normally ~120/80 mmHg in a young adult.
    """

    type: Optional[Any] = ["Category:OSW884b95065e355545b9ad5d495e65a1ea"]



class MassicPower(SpecificPower):
    """
    Quotient Energie durch Zeit und durch zugehöriger Masse
    """

    type: Optional[Any] = ["Category:OSWc8acb208c98359d282bf6f2a59af4e15"]



class ReactorTimeConstant(Time):
    """
    The "Reactor Time Constant", also called the reactor period, is the time during which the neutron flux density in a reactor changes by the factor e = 2.718 (e: basis of natural logarithms), when the neutron flux density increases or decreases exponentially.
    """

    type: Optional[Any] = ["Category:OSW6bf46ca1fcca5886971f9f2c9119a4a7"]



class Pressure(ForcePerArea):
    """
    Pressure is an effect which occurs when a force is applied on a surface. Pressure is the amount of force acting on a unit area. Pressure is distinct from stress, as the former is the ratio of the component of force normal to a surface to the surface area. Stress is a tensor that relates the vector force to the vector area.
    """

    type: Optional[Any] = ["Category:OSWb58cb5a4654f52e1804c74c035d21352"]



class Prevalence(DimensionlessRatio):
    """
    In epidemiology, prevalence is the proportion of a particular population found to be affected by a medical condition (typically a disease or a risk factor such as smoking or seatbelt use) at a specific time. (Wikipedia)
    """

    type: Optional[Any] = ["Category:OSW8ae4971bbbb15913a90c0f6a1075e2ae"]



class InitialNozzleThroatDiameter(NozzleThroatDiameter):
    """
    This is an autogenerated partial class definition of 'InitialNozzleThroatDiameter'
    """

    type: Optional[Any] = ["Category:OSWcb024afeb31e5a9abdb9f48b2ccb6983"]



class ColdReceptorThreshold(Temperature):
    """
    "Cold Receptor Threshold" is the threshold of cold-sensitive free nerve-ending.
    """

    type: Optional[Any] = ["Category:OSW364dc3047ad852c2bbee26d77fb270ab"]



class EquivalentDensity(Density):
    """
    "Equivalent Density" is the mass of a substance that reacts with (or is equivalent to) an arbitrary mass of
    another substance in a given chemical reaction, per volume.
    """

    type: Optional[Any] = ["Category:OSW264c76d5ade353bea3e1ab65437ff187"]



class HyperfineStructureQuantumNumber(QuantumNumber):
    """
    The "Hyperfine Structure Quantum Number" is a quantum number of an atom describing inclination of the nuclear spin with respect to a quantization axis given by the magnetic field produced by the orbital electrons.
    """

    type: Optional[Any] = ["Category:OSW565ff6d76da856d7aa3eb96993ecadd5"]



class AreaRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'AreaRatio'
    """

    type: Optional[Any] = ["Category:OSW1e2d83c5660e50828bd14194ea5d5717"]


class SolidAngle(AreaRatio):
    """
    The solid angle subtended by a surface S is defined as the surface area of a unit sphere covered by the surface S's projection onto the sphere. A solid angle is related to the surface of a sphere in the same way an ordinary angle is related to the circumference of a circle. Since the total surface area of the unit sphere is 4*pi, the measure of solid angle will always be between 0 and 4*pi.
    """

    type: Optional[Any] = ["Category:OSW180b2bc609d15ed7a4e6b95a952dfb05"]



class AmountOfSubstanceOfConcentration(Concentration):
    """
    "Amount of Substance of Concentration of B" is defined as the amount of a constituent divided by the volume of the mixture.
    """

    type: Optional[Any] = ["Category:OSWec3d914b6db25306838489afb9a45cc8"]



class ReynoldsNumber(DimensionlessRatio):
    """
    The "Reynolds Number" (Re) is a dimensionless number that gives a measure of the ratio of inertial forces to viscous forces and consequently quantifies the relative importance of these two types of forces for given flow conditions.
    """

    type: Optional[Any] = ["Category:OSW21be91e0703b56c6a6d996756c8e23a8"]



class GapEnergy(Energy):
    """
    "Gap Energy" is the difference in energy between the lowest level of conduction band and the highest level of valence band. It is an energy range in a solid where no electron states can exist.
    """

    type: Optional[Any] = ["Category:OSW78b09fe474c85bf09529d7eb3db0fe78"]


class SuperconductorEnergyGap(GapEnergy):
    """
    "Superconductor Energy Gap" is the width of the forbidden energy band in a superconductor.
    """

    type: Optional[Any] = ["Category:OSW3914f80e373d5d1f9a6df3a8643ce608"]



class ResonanceEnergy(Energy):
    """
    "Resonance Energy" in a nuclear reaction, is the kinetic energy of an incident particle, in the reference frame of the target, corresponding to a resonance in a nuclear reaction.
    """

    type: Optional[Any] = ["Category:OSW0299be3f8ccc586fb2975ad954b2e3bd"]



class MaximumExpectedOperatingThrust(MaxOperatingThrust):
    """
    This is an autogenerated partial class definition of 'MaximumExpectedOperatingThrust'
    """

    type: Optional[Any] = ["Category:OSW3a1dd757be6a5b38a8162d302f407238"]



class Altitude(Length):
    """
    Altitude or height is defined based on the context in which it is used (aviation, geometry, geographical survey, sport, and more). As a general definition, altitude is a distance measurement, usually in the vertical or "up" direction, between a reference datum and a point or object. The reference datum also often varies according to the context. [Wikipedia]
    """

    type: Optional[Any] = ["Category:OSW2423ce4a8e5c5a2782492fd72d06ee04"]


class ElevationRelativeToNap(Altitude):
    """
    Height measurement relative to the Normaal Amsterdams Peil (NAP) (en: Amsterdam Ordnance System). Being a form of gravity related height
    """

    type: Optional[Any] = ["Category:OSWca3e2877dac85f00baefb338479a3c44"]



class EllipticalOrbitApogeeVelocity(VehicleVelocity):
    """
    Velocity at apogee for an elliptical orbit velocity
    """

    type: Optional[Any] = ["Category:OSW21ffdd97a09d5fa5aec491d06ece05e8"]



class AngularDistance(Angle):
    """
    Angular distance travelled by orbiting vehicle measured from the azimuth of closest approach.
    """

    type: Optional[Any] = ["Category:OSW95c5ca7cd32d588aa490d8bc28e9cbb8"]



class CharacteristicNumber(Dimensionless):
    """
    Größe der Dimension 1 (als Ergebnis der metrisierenden Messtheorie), die Sachverhalte, Zustände oder Entwicklungen verdeutlicht und als Maßstab dient, um z. B. Ursache und Wirkung von Vorgängen in kausalem Zusammenhang darzustellen
    """

    type: Optional[Any] = ["Category:OSW5655587464525ab59c9d0f03d982c365"]



class ElectromotiveForce(EnergyPerElectricCharge):
    """
    In physics, $\textit{Electromotive Force}$, or most commonly $emf$ (seldom capitalized), or (occasionally) electromotance is that which tends to cause current (actual electrons and ions) to flow.
      More formally, $emf$ is the external work expended per unit of charge to produce an electric potential difference across two open-circuited terminals.
      $\textit{Electromotive Force}$ is deprecated in the ISO System of Quantities.
    """

    type: Optional[Any] = ["Category:OSW2ea2a195a92e5232854deeb78edf3b6f"]



class EffectiveExhaustvelocity(Velocity):
    """
    The velocity of an exhaust stream after reduction by effects such as friction, non-axially directed flow, and pressure differences between the inside of the rocket and its surroundings. The effective exhaust velocity is one of two factors determining the thrust, or accelerating force, that a rocket can develop, the other factor being the quantity of reaction mass expelled from the rocket in unit time. In most cases, the effective exhaust velocity is close to the actual exhaust velocity.
    """

    type: Optional[Any] = ["Category:OSWee6fb4bbbb50537c9b1ccd0e9f7d826a"]



class TotalCrossSection(CrossSection):
    """
    "Total Cross-section" is related to the absorbance of the light intensity through Beer-Lambert's law. It is the sum of all cross-sections corresponding to the various reactions or processes between an incident particle of specified type and energy and a target particle.
    """

    type: Optional[Any] = ["Category:OSW198956c936105dd0834746aef5674329"]



class ThermodynamicEntropy(EnergyPerTemperature):
    """
    Thermodynamic Entropy is a measure of the unavailability of a system’s energy to do work. It is a measure of the randomness of molecules in a system and is central to the second law of thermodynamics and the fundamental thermodynamic relation, which deal with physical processes and whether they occur spontaneously. The dimensions of entropy are energy divided by temperature, which is the same as the dimensions of Boltzmann's constant ($kB$) and heat capacity. The SI unit of entropy is $joule\ per\ kelvin$. [Wikipedia]
    """

    type: Optional[Any] = ["Category:OSW4ad1f3c1a959552294ad362006061b37"]



class MolarInternalEnergy(MolarEnergy):
    """
    This is an autogenerated partial class definition of 'MolarInternalEnergy'
    """

    type: Optional[Any] = ["Category:OSWcd40c1d85109521da9cb3b34f13e2671"]



class RealPartOfComplexFrequency(Frequency):
    """
    This is an autogenerated partial class definition of 'RealPartOfComplexFrequency'
    """

    type: Optional[Any] = ["Category:OSW586b905dcd825d0ca94fe79a97b6f229"]



class EquivalentAbsorptionArea(Area):
    """
    In a diffuse sound field, the Equivalent Absorption Area is that area of a surface having an absorption factor equal to 1, which, if diffraction effects are neglected, would, in the same diffuse sound field, absorb the same power.
    """

    type: Optional[Any] = ["Category:OSW859386b9a6c05411827a4f23d1bb6dc6"]



class ModulusOfLinearSubgradeReaction(ForcePerArea):
    """
    Modulus of Linear Subgrade Reaction is a measure for modulus of linear subgrade reaction, which expresses the elastic bedding of a linear structural element per length, such as for a beam. It is typically measured in N/m^2
    """

    type: Optional[Any] = ["Category:OSWebf10f70d7775b28ab44f8fcecbd8b16"]



class DewPointTemperature(Temperature):
    """
    "Dew Point Temperature" is the temperature at which vapour in air reaches saturation.
    """

    type: Optional[Any] = ["Category:OSW8d34f0cc11e758bfa887aa0be724fe4e"]



class PartialPressure(Pressure):
    """
    "Partial Pressure" is the pressure that the gas would have if it alone occupied the volume of the mixture at the same temperature.
    """

    type: Optional[Any] = ["Category:OSW9bf4b48d351a56e9a123cd93d798ef12"]



class NeelTemperature(Temperature):
    """
    "Neel Temperature" is the critical thermodynamic temperature of an antiferromagnet.
    """

    type: Optional[Any] = ["Category:OSWf27cc09849a154f087e42dcf5354c5c6"]



class VolumeFraction(DimensionlessRatio):
    """
    "Volume Fraction" is the volume of a constituent divided by the volume of all constituents of the mixture prior to mixing. Volume fraction is also called volume concentration in ideal solutions where the volumes of the constituents are additive (the volume of the solution is equal to the sum of the volumes of its ingredients).
    """

    type: Optional[Any] = ["Category:OSW642aecc3cec25d4ebc4a1b03ff1ae672"]



class AtmosphericPressure(Pressure):
    """
    The pressure exerted by the weight of the air above it at any point on the earth's surface. At sea level the atmosphere will support a column of mercury about $760 mm$ high. This decreases with increasing altitude. The standard value for the atmospheric pressure at sea level in SI units is $101,325 pascals$.
    """

    type: Optional[Any] = ["Category:OSWb250ea4742a35a81b710d43df474fe28"]



class PredictedMass(Mass):
    """
    Sum of the basic mass and the MGA. Current prediction of the final mass based on the current requirements and design.
    """

    type: Optional[Any] = ["Category:OSW265b3829c9da5f26bdf317a973c6ceca"]



class WebTimeAverageThrust(Thrust):
    """
    This is an autogenerated partial class definition of 'WebTimeAverageThrust'
    """

    type: Optional[Any] = ["Category:OSWe5068aa8fec252a2803f5ecf06a90cbb"]



class RelativeMolecularMass(DimensionlessRatio):
    """
    "Relative Molecular Mass " is equivalent to the numerical value of the molecular mass expressed in unified atomic mass units. The molecular mass (m) is the mass of a molecule.
    """

    type: Optional[Any] = ["Category:OSW41a3138364035cff84c064b3ab52e6a4"]



class FermiEnergy(Energy):
    """
    "Fermi Energy" in a metal is the highest occupied energy level at zero thermodynamic temperature.
    """

    type: Optional[Any] = ["Category:OSW76e5322d7b8c5f03be94ad8dc87405b1"]



class Stress(ForcePerArea):
    """
    Stress is a measure of the average amount of force exerted per unit area of a surface within a deformable body on which internal forces act. In other words, it is a measure of the intensity or internal distribution of the total internal forces acting within a deformable body across imaginary surfaces. These internal forces are produced between the particles in the body as a reaction to external forces applied on the body. Stress is defined as ${\rm{Stress}} = \frac{F}{A}$.
    """

    type: Optional[Any] = ["Category:OSW74ae1de66beb525ea52eedabf09ab228"]



class SecondStageMassRatio(MassRatio):
    """
    Mass ratio for the second stage of a multistage launcher.
    """

    type: Optional[Any] = ["Category:OSW85cb752c0cb7520b9217206d5efe1858"]



class Azimuth(Angle):
    """
    The horizontal angle between an object and a cardinal direction, generally north.
      In the context of architecture, this would refer to the direction a structure faces relative to the direction north.
    """

    type: Optional[Any] = ["Category:OSWd912fbf90a895d568036bb01e07fe232"]



class LuminousEmmitance(LuminousFluxPerArea):
    """
    "Luminous Emittance" is the luminous flux per unit area emitted from a surface.
    """

    type: Optional[Any] = ["Category:OSWc90b3cc08a04506697aeca7645bc47dd"]



class AlphaDisintegrationEnergy(Energy):
    """
    The "Alpha Disintegration Energy" is the sum of the kinetic energy of the alpha-particle produced in the disintegration process and the recoil energy of the product atom in the reference frame in which the emitting nucleus is at rest before its disintegration.
    """

    type: Optional[Any] = ["Category:OSWfe05b78a868b51be8f9bcc20d5778090"]



class OrbitalAngularMomentumQuantumNumber(QuantumNumber):
    """
    The "Principal Quantum Number" describes the electron shell, or energy level, of an atom. The value of $n$ ranges from 1 to the shell containing the outermost electron of that atom.
    """

    type: Optional[Any] = ["Category:OSW5c36ed49914c5294ab829feb052f5cdb"]



class HalfLife(Time):
    """
    The "Half-Life" is the average duration required for the decay of one half of the atoms or nuclei.
    """

    type: Optional[Any] = ["Category:OSW22e788fd36bc5f8d9007e46b1b874413"]



class MutualInductance(Inductance):
    """
    $\textit{Mutual Inductance}$ is the non-diagonal term of the inductance matrix. For two loops, the symbol $M$ is used for $L_{12}$.
    """

    type: Optional[Any] = ["Category:OSW51cb2a0565745eee958c6ede005561d8"]



class GaugePressure(Pressure):
    """
    Gauge Pressure is the pressure of a system relative to the pressure of the surrounding atmosphere.
    It is the difference between the absolute pressure and the atmospheric pressure. Gauge pressure is positive for pressures
    above atmospheric pressure and negative for pressures below it. A Quantity in QUDT having a QuantityKind of GaugePressure
    would typically also assert the value of qudt:isDeltaQuantity to be true, indicating that the value is a difference between
    two pressures.
    """

    type: Optional[Any] = ["Category:OSW9807945ef51e5e71af339c5b6984f693"]



class ClosestApproachRadius(Radius):
    """
    This is an autogenerated partial class definition of 'ClosestApproachRadius'
    """

    type: Optional[Any] = ["Category:OSWcef8c92a98b15f3ab49be706ef200090"]



class VerticalVelocity(Velocity):
    """
    The rate at which a body moves upwards at an angle of 90 degrees to the ground. It is the component of a projectile's velocity which is concerned with lifting the projectile.
    """

    type: Optional[Any] = ["Category:OSW8d942272762357159c766f3a5a7f29c5"]



class Angle(DimensionlessRatio):
    """
    The abstract notion of angle. Narrow concepts include plane angle and solid angle. While both plane angle and solid angle are dimensionless, they are actually length/length and area/area respectively.
    """

    type: Optional[Any] = ["Category:OSW2339256af71e5635a541ac7f5a437141"]



class WaterHorsepower(Power):
    """
    No pump can convert all of its mechanical power into water power. Mechanical power is lost in the pumping process due to friction losses and other physical losses. It is because of these losses that the horsepower going into the pump has to be greater than the water horsepower leaving the pump. The efficiency of any given pump is defined as the ratio of the water horsepower out of the pump compared to the mechanical horsepower into the pump.
    """

    type: Optional[Any] = ["Category:OSW0a6d4ab2792f569da06af40abdb83759"]



class TemperatureRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'TemperatureRatio'
    """

    type: Optional[Any] = ["Category:OSW7f104091cb7f50aea7e4ad58065ef4fb"]



class DiffusionLength(Length):
    """
    "Diffusion Length" is the average distance traveled by a particle, or a thermal neutron in a nuclear reactor, from the point at which it is formed to the point at which it is absorbed.
    """

    type: Optional[Any] = ["Category:OSW4d3cf91b99bc5413a41b88cf3c1a814c"]



class MaxSeaLevelThrust(Thrust):
    """
    This is an autogenerated partial class definition of 'MaxSeaLevelThrust'
    """

    type: Optional[Any] = ["Category:OSW79efc6b7a03a5e5eb6bdfc8e6bf1056c"]



class IonConcentration(InverseVolume):
    """
    "Ion Concentration" is the number of ions per unit volume. Also known as ion density.
    """

    type: Optional[Any] = ["Category:OSW0e8c5f1a905350ccbc8145c63ae0d57c"]



class MoistureDiffusivity(VolumeFlowRate):
    """
    This is an autogenerated partial class definition of 'MoistureDiffusivity'
    """

    type: Optional[Any] = ["Category:OSWfdce4febeb155bd290622a7a78f0fbba"]



class PressureRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'PressureRatio'
    """

    type: Optional[Any] = ["Category:OSW7014422ed34957de9d4ca0fb6e3d74d3"]



class WebTime(Time):
    """
    This is an autogenerated partial class definition of 'WebTime'
    """

    type: Optional[Any] = ["Category:OSW02ed3a478531578b90f11bcaefa3f86c"]



class SurfaceTension(EnergyPerArea):
    """
    "Surface Tension" is a contractive tendency of the surface of a liquid that allows it to resist an external force.
    """

    type: Optional[Any] = ["Category:OSW15f7a6141937572f97eac08557b488ce"]



class SignalStrength(ElectricFieldStrength):
    """
    In telecommunications, particularly in radio, signal strength refers to the magnitude of the electric field at a reference point that is a significant distance from the transmitting antenna. It may also be referred to as received signal level or field strength. Typically, it is expressed in voltage per length or signal power received by a reference antenna. High-powered transmissions, such as those used in broadcasting, are expressed in dB-millivolts per metre (dBmV/m).
    """

    type: Optional[Any] = ["Category:OSW2b4e65f26005511487ca6d47b859e932"]



class SoundParticleDisplacement(Length):
    """
    Sound Particle Displacement is the nstantaneous displacement of a particle in a medium from what would be its position in the absence of sound waves.
    """

    type: Optional[Any] = ["Category:OSW7ceec259ea9e577087a670ecd631ab27"]



class MechanicalEnergy(Energy):
    """
    Mechanical Energy is the sum of potential energy and kinetic energy. It is the energy associated with the motion and position of an object.
    """

    type: Optional[Any] = ["Category:OSW7f4e4ae7033a51d2903c951e9efd306b"]



class StochasticProcess(Frequency):
    """
    In probability theory, a stochastic process, or sometimes random process  is a collection of random variables; this is often used to represent the evolution of some random value, or system, over time. This is the probabilistic counterpart to a deterministic process (or deterministic system).
    """

    type: Optional[Any] = ["Category:OSWbec1168058375097b6157eb8ac35eab4"]


class Activity(StochasticProcess):
    """
    $\textit{Activity}$ is the number of decays per unit time of a radioactive sample,
       the term used to characterise the number of nuclei which disintegrate in a radioactive substance per unit time.
      Activity is usually measured in Becquerels ($Bq$), where 1 $Bq$ is 1 disintegration per second,
       in honor of the scientist Henri Becquerel.
    """

    type: Optional[Any] = ["Category:OSWe45bd0c8c7c8527da9d31b11e061b60a"]



class ParticlePositionVector(Length):
    """
    "Particle Position Vector" is the position vector of a particle.
    """

    type: Optional[Any] = ["Category:OSWc2570a8ce0a65454a303491826ff7617"]



class PrincipalQuantumNumber(QuantumNumber):
    """
    The "Principal Quantum Number" describes the electron shell, or energy level, of an atom. The value of $n$ ranges from 1 to the shell containing the outermost electron of that atom.
    """

    type: Optional[Any] = ["Category:OSW83c669868aad5ac5a74cc377907c78d3"]



class HelmholtzEnergy(Energy):
    """
    $\textit{Helmholtz Energy}$ is one of the potentials are used to measure energy changes in systems as they evolve from an initial state to a final state. The potential used depends on the constraints of the system, such as constant temperature or pressure. $\textit{Internal Energy}$ is the internal energy of the system, $\textit{Enthalpy}$ is the internal energy of the system plus the energy related to pressure-volume work, and Helmholtz and Gibbs free energy are the energies available in a system to do useful work when the temperature and volume or the pressure and temperature are fixed, respectively. The name $\textit{Helmholz Free Energy}$ is also used.
    """

    type: Optional[Any] = ["Category:OSW7cf1f3076962552cbe8028e61a15af53"]



class IsothermalMoistureCapacity(SpecificVolume):
    """
    "Isothermal Moisture Capacity" is the capacity of a material to absorb moisture in the Effective Moisture Penetration Depth (EMPD) model.
    """

    type: Optional[Any] = ["Category:OSW3cd5a69656f4590194bbbfc7cfa614fb"]



class ThermodynamicEnergy(Energy):
    """
    This is an autogenerated partial class definition of 'ThermodynamicEnergy'
    """

    type: Optional[Any] = ["Category:OSWe58e83b511355b999aa0dcb40428df2a"]



class HorizontalVelocity(Velocity):
    """
    Component of a projectile's velocity, which acts parallel to the ground and does not lift the projectile in the air.
    """

    type: Optional[Any] = ["Category:OSW6713dc0ce346512595f2d28e8f6bd8bb"]



class HeatCapacity(EnergyPerTemperature):
    """
    "Heat Capacity" (usually denoted by a capital $C$, often with subscripts), or thermal capacity, is the measurable physical quantity that characterizes the amount of heat required to change a substance's temperature by a given amount. In the International System of Units (SI), heat capacity is expressed in units of joule(s) (J) per kelvin (K).
    """

    type: Optional[Any] = ["Category:OSW3601c7fff2f75532a538c5b82165a134"]



class PolarMomentOfInertia(MomentOfInertia):
    """
    The polar moment of inertia is a quantity used to predict an object's ability to resist torsion, in objects (or segments of objects) with an invariant circular cross-section and no significant warping or out-of-plane deformation. It is used to calculate the angular displacement of an object subjected to a torque. It is analogous to the area moment of inertia, which characterizes an object's ability to resist bending.
    """

    type: Optional[Any] = ["Category:OSWbf23a3447dad5d69bc7a45ab4de68e83"]



class DeltaV(Velocity):
    """
    The change in translational velocity including all losses for a propulsive system or module. Delta-V losses include, but are not limited to, gravity losses and steering losses.
    """

    type: Optional[Any] = ["Category:OSWc6e4b85acce153fd85a0b7babd166131"]



class CharacteristicVelocity(Velocity):
    """
    Characteristic velocity or $c^{*}$ is a measure of the combustion performance of a rocket engine independent of nozzle performance, and is used to compare different propellants and propulsion systems.
    """

    type: Optional[Any] = ["Category:OSW06321a3ed4165337a8fc380a77a64e09"]



class IonizationEnergy(Energy):
    """
    "Ionization Energy" is the energy difference between an electron at rest at infinity and an electron at a certain energy level. The amount of energy required to remove an electron from that atom or molecule in the gas phase.
    """

    type: Optional[Any] = ["Category:OSW510287e6716f5be098e9ad2c80ea3d4f"]


class AcceptorIonizationEnergy(IonizationEnergy):
    """
    "Acceptor Ionization Energy" is the ionization energy of an acceptor.
    """

    type: Optional[Any] = ["Category:OSWc0f0bce2b2765c13898ecb55bde6cd0f"]



class WorkFunction(Energy):
    """
    "Work Function" is the energy difference between an electron at rest at infinity and an electron at a certain energy level. The minimum energy (usually measured in electronvolts) needed to remove an electron from a solid to a point immediately outside the solid surface (or energy needed to move an electron from the Fermi level into vacuum).
    """

    type: Optional[Any] = ["Category:OSWf9f89e877cfa5aefa59c208b25b14754"]



class Vorticity(AngularVelocity):
    """
    In the simplest sense, vorticity is the tendency for elements of a fluid to "spin." More formally, vorticity can be related to the amount of "circulation" or "rotation" (or more strictly, the local angular rate of rotation) in a fluid. The average vorticity in a small region of fluid flow is equal to the circulation C around the boundary of the small region, divided by the area A of the small region. Mathematically, vorticity is a vector field and is defined as the curl of the velocity field.
    """

    type: Optional[Any] = ["Category:OSW55eac7b36313581b839d0bd4957f7788"]



class ThermalTransmittance(CoefficientOfHeatTransfer):
    """
    Thermal transmittance is the rate of transfer of heat through matter. The thermal transmittance of a material (such as insulation or concrete) or an assembly (such as a wall or window) is expressed as a U-value. The concept of thermal transmittance is closely related to that of thermal resistance. The thermal resistance of a structure is the reciprocal of its thermal transmittance.
    """

    type: Optional[Any] = ["Category:OSW72a50f1212bd568fb1acca74abad26e4"]



class IncidenceRate(Incidence):
    """
    The incidence rate is a measure of the frequency with which a disease or other incident occurs over a specified time period. It is also known as the incidence density rate or person-time incidence rate, when the denominator is the combined person-time of the population at risk (the sum of the time duration of exposure across all persons exposed)
    """

    type: Optional[Any] = ["Category:OSW877bfc2bdb1c5e19b67c4fede37fdb56"]



class BetaDisintegrationEnergy(Energy):
    """
    "Beta Disintegration Energy" is the  energy released by a beta particle radioactive decay. It is the sum of the maximum beta-particle kinetic energy and the recoil energy of the atom produced in the reference frame in which the emitting nucleus is at rest before its disintegration.
    """

    type: Optional[Any] = ["Category:OSW532bab2a81f451fb9dc34122da50dca6"]



class EquilibriumPositionVectorOfIon(Length):
    """
    "Equilibrium Position Vector of Ion" is the position vector of a particle in equilibrium.
    """

    type: Optional[Any] = ["Category:OSW75f2f083a2e856f3bd3757d099851530"]



class Strain(DimensionlessRatio):
    """
    In any branch of science dealing with materials and their behaviour, strain is the geometrical expression of deformation caused by the action of stress on a physical body. Strain is calculated by first assuming a change between two body states: the beginning state and the final state. Then the difference in placement of two points in this body in those two states expresses the numerical value of strain. Strain therefore expresses itself as a change in size and/or shape. [Wikipedia]
    """

    type: Optional[Any] = ["Category:OSW877f6c0b113452649d1a4ac5ea3a6710"]



class Irradiance(PowerPerArea):
    """
    Irradiance and Radiant Emittance are radiometry terms for the power per unit area of electromagnetic radiation at a surface. "Irradiance" is used when the electromagnetic radiation is incident on the surface. "Radiant emmitance" (or "radiant exitance") is used when the radiation is emerging from the surface.
    """

    type: Optional[Any] = ["Category:OSW4f181df1bf2d5e88a36fe5585cb10b8b"]



class IgnitionIntervalTime(Time):
    """
    This is an autogenerated partial class definition of 'IgnitionIntervalTime'
    """

    type: Optional[Any] = ["Category:OSW3323f81caeda5c7fb04fc95cdc3e4f68"]



class AmountOfSubstancePerVolume(Concentration):
    """
    The amount of substance per unit volume is called the molar density. Molar density is an intensive property of a substance and depends on the temperature and pressure.
    """

    type: Optional[Any] = ["Category:OSW98493d0d7b8b528fa42a2332c8cf502f"]


class WaterSolubility(AmountOfSubstancePerVolume):
    """
    An amount of substance per unit volume that is the concentration of a saturated solution expressed as the ratio of the solute concentration over the volume of water.  A substance's solubility fundamentally depends on several physical and chemical properties of the solution as well as the environment it is in.
    """

    type: Optional[Any] = ["Category:OSW9321ad05d637531b87fdaf5993788342"]



class MeanEnergyImparted(Energy):
    """
    The "Mean Energy Imparted", is the average energy imparted to irradiated matter.
    """

    type: Optional[Any] = ["Category:OSWe10431f5aa915640a353fadcefc0f3c2"]



class ActivePower(ComplexPower):
    r"""
    An $Active Power$ is, under periodic conditions, the mean value, taken over one period $T$, of the instantaneous power $p$.
      In complex notation, $P = \mathbf{Re} \; \underline{S}$, where $\underline{S}$ is $\textit{complex power}$.
    """

    type: Optional[Any] = ["Category:OSWd8d82c0906245817ad4c0d3d273e0b29"]



class VehicleVelocity(Velocity):
    """
    This is an autogenerated partial class definition of 'VehicleVelocity'
    """

    type: Optional[Any] = ["Category:OSW42543b13af4c5af88462e7ac8ff8707d"]



class SpecificEnergyImparted(SpecificEnergy):
    """
    The "Specific Energy Imparted", is the energy imparted to an element of irradiated matter divided by the mass, dm, of that element.
    """

    type: Optional[Any] = ["Category:OSW99368549565a5844b9210bc2acf27631"]



class DynamicFrictionCoefficient(FrictionCoefficient):
    """
    Kinetic (or dynamic) friction occurs when two objects are moving relative to each other and rub together (like a sled on the ground).
    """

    type: Optional[Any] = ["Category:OSW2fe5b0713ef45b6096fb35cb7085cfe7"]



class CartesianCoordinates(Length):
    """
    "Cartesian Coordinates" specify each point uniquely in a plane by a pair of numerical coordinates, which are the signed distances from the point to two fixed perpendicular directed lines, measured in the same unit of length.
    """

    type: Optional[Any] = ["Category:OSWc8457fe4bcf15a08881828cd270ddfa1"]



class NominalAscentPropellantMass(Mass):
    """
    The amount of propellant mass within a stage that is available for impulse for use in nominal payload performance prediction. This mass excludes loaded propellant that has been set aside for off- nominal performance behavior (FPR and fuel bias).
    """

    type: Optional[Any] = ["Category:OSWd5ff55bcf2105e6e9e7f4cf1bca75dad"]



class NeutralRatio(DimensionlessRatio):
    """
    Quotient aus zwei physikalischen Größen gleicher Art als Zahl, welche das Verhältnis dieser Größen zueinander ausdrückt, wobei die einheiten gegeneinander gekürzt sind
    """

    type: Optional[Any] = ["Category:OSW5b7237a62ecf55bf98b2c37be3ff75ab"]



class KineticOrThermalEnergy(Energy):
    """
    Energie, die in der Bewegung eines Körpers steckt und sich aus Translationsenergie und Rotationsenergie zusammen setzt, die durch die Bewegung dieses Körpers gegenüber einem anderen System und durch seine Masse (Massenverteilung) bestimmt wird oder Energie in Form von Wärme
    """

    type: Optional[Any] = ["Category:OSW2c2ac8c297a2545bb8a0d30f81bb6b8d"]



class LiquidVolume(Volume):
    """
    Liquid volume is the volume of a given amount of liquid, that is, the amount of space a liquid takes up. There are a number of different units used to measure liquid volume, but most of them fall under either the metric system of measurement or the Imperial system of measurement.
    """

    type: Optional[Any] = ["Category:OSWd4fab90301655967a4fda944db63c694"]



class RelativePartialPressure(PressureRatio):
    """
    This is an autogenerated partial class definition of 'RelativePartialPressure'
    """

    type: Optional[Any] = ["Category:OSW99edcb0bac12560fa33d6af42aecad67"]


class RelativeHumidity(RelativePartialPressure):
    """
    $\textit{Relative Humidity}$ is the ratio of the partial pressure of water vapor in an air-water mixture to the saturated vapor pressure of water at a prescribed temperature.
      The relative humidity of air depends not only on temperature but also on the pressure of the system of interest.
      $$$$
      $\textit{Relative Humidity}$ is also referred to as $\textit{Relative Partial Pressure}$.
      $$$$
      Relative partial pressure is often referred to as $RH$ and expressed in percent.
    """

    type: Optional[Any] = ["Category:OSWa07538ca42b95d669752f58ab5db755f"]



class AuditoryThresholds(SoundPowerLevel):
    """
    "Auditory Thresholds" is the thresholds of sensitivity to auditory signals and other input to the ear or the sense of hearing.
    """

    type: Optional[Any] = ["Category:OSWbb12910958f951daa14162c7078632f3"]



class ThermalDiffusivity(AreaPerTime):
    """
    In heat transfer analysis, thermal diffusivity (usually denoted $\alpha$ but $a$, $\kappa$,$k$, and $D$ are also used) is the thermal conductivity divided by density and specific heat capacity at constant pressure. The formula is: $\alpha = {k \over {\rho c_p}}$, where k is thermal conductivity ($W/(\mu \cdot K)$), $\rho$ is density ($kg/m^{3}$), and $c_p$ is specific heat capacity ($\frac{J}{(kg \cdot K)}$) .The denominator $\rho c_p$, can be considered the volumetric heat capacity ($\frac{J}{(m^{3} \cdot K)}$).
    """

    type: Optional[Any] = ["Category:OSW9f658cc25f6b5121957bbcc537814b30"]



class BendingMomentOfForce(Torque):
    """
    A bending moment exists in a structural element when a moment is applied to the element so that the element bends. It is the component of moment of force perpendicular to the longitudinal axis of a beam or a shaft.
    """

    type: Optional[Any] = ["Category:OSW3d007b21655e5a689b8ad512f768cd37"]



class AccelerationOfGravity(Acceleration):
    """
    The acceleration of freely falling bodies under the influence of terrestrial gravity, equal to approximately 9.81 meters (32 feet) per second per second.
    """

    type: Optional[Any] = ["Category:OSWef97c736e77c56a2808470c2bfd808dc"]



class Exposure(ElectricChargePerMass):
    """
    "Exposure" reflects the extent of ionization events taking place when air is irradiated by ionizing photons (gamma radiation and/or x rays). In photography, exposure is the amount of light allowed to fall on each area unit of a photographic medium (photographic film or image sensor) during the process of taking a photograph. Exposure is measured in lux seconds, and can be computed from exposure value (EV) and scene luminance in a specified region.
    """

    type: Optional[Any] = ["Category:OSWd41cd569a9fb561a8415b09d2d0af5f2"]



class ElectricalPowerToMassRatio(SpecificPower):
    """
    This is an autogenerated partial class definition of 'ElectricalPowerToMassRatio'
    """

    type: Optional[Any] = ["Category:OSW888d441794f35e2ca1219afab29d38d4"]



class MigrationArea(Area):
    """
    "Migration Area" is the sum of the slowing-down area from fission energy to thermal energy and the diffusion area for thermal neutrons.
    """

    type: Optional[Any] = ["Category:OSW1f5c6d48545a563989566d8b589612c2"]



class HeadEndPressure(Pressure):
    """
    This is an autogenerated partial class definition of 'HeadEndPressure'
    """

    type: Optional[Any] = ["Category:OSW31cf0c812f335d06a0fab1a15b46d6e5"]



class MassOfSolidBooster(Mass):
    """
    This is an autogenerated partial class definition of 'MassOfSolidBooster'
    """

    type: Optional[Any] = ["Category:OSW3805347ea7cc5372812c240ee9c72d57"]



class InertMass(Mass):
    """
    The sum of the vehicle dry mass, residual fluids and gasses, personnel and personnel provisions, and cargo.
    """

    type: Optional[Any] = ["Category:OSWa142144f1fb3549191b50f624bdcbb94"]



class ServiceFactor(DimensionlessRatio):
    """
    The value indicates the multiplier of the rated power that equipment can handle for some period of time when operating according to a manufacturer's specified conditions; typically applicable to motors.
    """

    type: Optional[Any] = ["Category:OSW878ac43af7e05aa7865088cb0b79caeb"]



class PositionVector(Length):
    """
    A "Position Vector", also known as location vector or radius vector, is a Euclidean vector which represents the position of a point P in space in relation to an arbitrary reference origin O.
    """

    type: Optional[Any] = ["Category:OSWd60aaf9b746a594a83805f0f0ae921ff"]



class ThrustToMassRatio(Acceleration):
    """
    This is an autogenerated partial class definition of 'ThrustToMassRatio'
    """

    type: Optional[Any] = ["Category:OSW993eb85e63035bd2bf24dafc18760215"]



class ElectricCurrentPerLength(LinearElectricCurrentDensity):
    """
    This is an autogenerated partial class definition of 'ElectricCurrentPerLength'
    """

    type: Optional[Any] = ["Category:OSW8ba7ac8b06c453e2885cc41c9d9ee0bb"]



class Loudness(Dimensionless):
    """
    Maß für die Stärke der subjektiven Hörempfindung, welche auf einer Skala "leise-laut" in sone skaliert wird; einer frei fortschreitenden monofrequenten Welle mit der Frequenz 1 kHz und dem Schalldruckpegel 40 dB, die frontal auf die Zuhörer trifft, ist die Lautheit 1 sone zugeordnet und ein Laut, welcher von den Zuhörern als n-mal so laut wie derjenige mit 1 sone bezeichnet wird, erhält die Lautheit n sone zugeordnet
    """

    type: Optional[Any] = ["Category:OSW7deca0ab21f751e3b59b71d86b890f0d"]



class TemperatureRateOfChange(TemperaturePerTime):
    """
    The "Temperature Rate of Change" measures the difference of a temperature per time (positive: rise, negative: fall), as for instance used with heat sensors. It is for example measured in K/s.
    """

    type: Optional[Any] = ["Category:OSWa04307c2ccbf57d0b16281a3be595f60"]



class DebyeAngularFrequency(AngularFrequency):
    """
    "Debye Angular Frequency" is the cut-off angular frequency in the Debye model of the vibrational spectrum of a solid.
    """

    type: Optional[Any] = ["Category:OSWa284f00a432c5ca09e8b1c61eb0d30ed"]



class SpecificHeatsRatio(DimensionlessRatio):
    """
    The ratio of specific heats, for the exhaust gases adiabatic gas constant, is the relative amount of compression/expansion energy that goes into temperature $T$ versus pressure $P$ can be characterized by the heat capacity ratio: $\gamma\frac{C_P}{C_V}$, where $C_P$ is the specific heat (also called heat capacity) at constant pressure, while $C_V$ is the specific heat at constant volume.
    """

    type: Optional[Any] = ["Category:OSWa2a96072e46a57b2a36f0510ac8a5fbb"]



class ApparentPower(ComplexPower):
    """
    "Apparent Power" is the product of the rms voltage $U$ between the terminals of a two-terminal element or two-terminal circuit and the rms electric current I in the element or circuit. Under sinusoidal conditions, the apparent power is the modulus of the complex power.
    """

    type: Optional[Any] = ["Category:OSW9a9b930a8a175c13925e18bea1363e3a"]



class Efficiency(DimensionlessRatio):
    """
    Efficiency is the ratio of output power to input power.
    """

    type: Optional[Any] = ["Category:OSW8cccae8a45095dcd89a769a33373731a"]



class AmbientPressure(Pressure):
    """
    The ambient pressure on an object is the pressure of the surrounding medium, such as a gas or liquid, which comes into contact with the object.
    The SI unit of pressure is the pascal (Pa), which is a very small unit relative to atmospheric pressure on Earth, so kilopascals ($kPa$) are more commonly used in this context.
    """

    type: Optional[Any] = ["Category:OSW2db9d2e24c985062b5f764ebc6e146fb"]



class SpinQuantumNumber(QuantumNumber):
    """
    The "Spin Quantum Number"  describes the spin (intrinsic angular momentum) of the electron within that orbital, and gives the projection of the spin angular momentum S along the specified axis
    """

    type: Optional[Any] = ["Category:OSWda012dbe914456a09af4429dce5dcc49"]



class AcousticImpediance(MassPerAreaTime):
    """
    Acoustic impedance at a surface is the complex quotient of the average sound pressure over that surface by the sound volume flow rate through that surface.
    """

    type: Optional[Any] = ["Category:OSW1122e0bc34a9581faea31f6967f701d6"]



class SoundPressure(Pressure):
    """
    Sound Pressure is the difference between instantaneous total pressure and static pressure.
    """

    type: Optional[Any] = ["Category:OSW28f9a77b22c65003b5d7e23a5d938191"]



class LatticeVector(Length):
    """
    "Lattice Vector" is a translation vector that maps the crystal lattice on itself.
    """

    type: Optional[Any] = ["Category:OSWff95a9d808375e7c9631c797e43546cd"]



class MagneticFieldStrength(ElectricCurrentPerLength):
    """
    $\textit{Magnetic Field Strength}$ is a vector quantity obtained at a given point by subtracting the magnetization $M$ from the magnetic flux density $B$ divided by the magnetic constant $\mu_0$. The magnetic field strength is related to the total current density $J_{tot}$ via: $\text{rot} H = J_{tot}$.
    """

    type: Optional[Any] = ["Category:OSW5066212adfda5519af307363bd1c5c79"]



class Count(Dimensionless):
    """
    "Count" is the value of a count of items.
    """

    type: Optional[Any] = ["Category:OSWb0250d3677f6592f9d4329c8b9d5f8d1"]



class MagneticQuantumNumber(QuantumNumber):
    """
    The "Magnetic Quantum Number" describes the specific orbital (or "cloud") within that subshell, and yields the projection of the orbital angular momentum along a specified axis.
    """

    type: Optional[Any] = ["Category:OSW42786048fcdf5843a54bde7957c34c5e"]



class VolumeFlowRatio(DimensionlessRatio):
    """
    Volume flow ratio is commonly used in fluid dynamics and engineering,
      referring to the ratio of the flow rates of two or more fluid streams within a system. In HVAC systems,
      the flow ratio could compare the amount of fresh air introduced to the amount of recirculated air.
    """

    type: Optional[Any] = ["Category:OSW91098185e0b250609beefef37c7e1fe0"]



class NormalStress(Stress):
    """
    Normal stress is defined as the stress resulting from a force acting normal to a body surface. Normal stress can be caused by several loading methods, the most common being axial tension and compression, bending, and hoop stress.
    """

    type: Optional[Any] = ["Category:OSWa8a9a4780dcd56dba67af825f452aaad"]



class LiftCoefficient(Dimensionless):
    """
    The lift coefficient is a dimensionless coefficient that relates the lift generated by a lifting body, the dynamic pressure of the fluid flow around the body, and a reference area associated with the body.
    """

    type: Optional[Any] = ["Category:OSW2db5f26f631554fa840ba5d0533ec86f"]



class LowerCriticalMagneticFluxDensity(MagneticFluxDensity):
    """
    "Lower Critical Magnetic Flux Density" for type II superconductors, is the threshold magnetic flux density for magnetic flux entering the superconductor.
    """

    type: Optional[Any] = ["Category:OSWe54917d49a3b5a02b60f280f68490fa4"]



class HeatFluxDensity(PowerPerArea):
    """
    This is an autogenerated partial class definition of 'HeatFluxDensity'
    """

    type: Optional[Any] = ["Category:OSW8bd1dddac6c45418afac16180d92978d"]



class DebyeTemperature(Temperature):
    """
    "Debye Temperature" is the temperature at which the highest-frequency mode (and hence all modes) are excited.
    """

    type: Optional[Any] = ["Category:OSWbb7902b209065fa5858183c383ed4254"]



class BucklingFactor(Dimensionless):
    """
    This is an autogenerated partial class definition of 'BucklingFactor'
    """

    type: Optional[Any] = ["Category:OSW3e723f9b78635333a501ab96ea78c49f"]



class RelativeAtomicMass(DimensionlessRatio):
    """
    "Relative Atomic Mass " is a dimensionless physical quantity, the ratio of the average mass of atoms of an element (from a given source) to 1/12 of the mass of an atom of carbon-12 (known as the unified atomic mass unit)
    """

    type: Optional[Any] = ["Category:OSW1e5c0baddb355cd591ec727ff16e88d9"]



class AngleOfOpticalRotation(Angle):
    """
    The "Angle of Optical Rotation" is the angle through which plane-polarized light is rotated clockwise, as seen when facing the light source, in passing through an optically active medium.
    """

    type: Optional[Any] = ["Category:OSW63d076aa990f55acbc4b36a07dbd99e9"]



class ConductionSpeed(Speed):
    """
    "Conduction Speed" is the speed of impulses in nerve fibers.
    """

    type: Optional[Any] = ["Category:OSW2a1c80f8e8fb5867b9e138bbaf83d105"]



class StaticPressure(Pressure):
    """
    "Static Pressure" is the pressure at a nominated point in a fluid. Every point in a steadily flowing fluid, regardless of the fluid speed at that point, has its own static pressure $P$, dynamic pressure $q$, and total pressure $P_0$. The total pressure is the sum of the dynamic and static pressures, that is $P_0 = P + q$.
    """

    type: Optional[Any] = ["Category:OSW9730894285945607baf909d27f80638e"]



class HalfValueThickness(Length):
    """
    The "Half-Value Thickness" is the thickness of the material at which the intensity of radiation entering it is reduced by one half.
    """

    type: Optional[Any] = ["Category:OSW3c905c5ff4875816b88278e68e643c27"]



class WetBulbTemperature(Temperature):
    """
    the temperature of a parcel of air cooled to saturation (100% relative humidity) by the evaporation of water into it, with the latent heat supplied by the parcel.
    """

    type: Optional[Any] = ["Category:OSW343daa86363c5bda9ac91f20c65eede0"]



class CenterOfGravityInTheXAxis(Length):
    """
    This is an autogenerated partial class definition of 'CenterOfGravityInTheXAxis'
    """

    type: Optional[Any] = ["Category:OSW89d1a9df9ae256df9c0fdf46b74cb96b"]



class CenterOfGravityInTheYAxis(Length):
    """
    This is an autogenerated partial class definition of 'CenterOfGravityInTheYAxis'
    """

    type: Optional[Any] = ["Category:OSWc0856531473456db89ce4276f30ca062"]



class Illuminance(LuminousFluxPerArea):
    """
    Illuminance is the total luminous flux incident on a surface, per unit area. It is a measure of the intensity of the incident light, wavelength-weighted by the luminosity function to correlate with human brightness perception.
    """

    type: Optional[Any] = ["Category:OSW0e767858fc7a5df0a3be780057b78446"]



class InitialExpansionRatio(ExpansionRatio):
    """
    This is an autogenerated partial class definition of 'InitialExpansionRatio'
    """

    type: Optional[Any] = ["Category:OSW47c1c967b7fe517f95d3d969aade0e12"]



class TemperatureDifference(Temperature):
    """
    Temperature difference (Delta T) is the difference of temperatures between two measuring points
    """

    type: Optional[Any] = ["Category:OSW0ec63b2885715618b4e7ffdba2987af8"]



class AbsoluteHumidity(Density):
    """
    $\textit{Absolute Humidity}$ is an amount of water vapor, usually discussed per unit volume.
      Absolute humidity in air ranges from zero to roughly 30 grams per cubic meter when the air is saturated at $30 ^\circ C$.
      The absolute humidity changes as air temperature or pressure changes.
      $$$$
      This is very inconvenient for chemical engineering calculations, e.g. for clothes dryers, where temperature can vary considerably.
      As a result, absolute humidity is generally defined in chemical engineering as mass of water vapor per unit mass of dry air,
       also known as the mass mixing ratio, which is much more rigorous for heat and mass balance calculations.
      $$$$
      Mass of water per unit volume as in the equation above would then be defined as volumetric humidity, because of the potential confusion.
    """

    type: Optional[Any] = ["Category:OSW905e0bae40465f95ba62564fdb8f1c47"]



class NuclearEnergy(Energy):
    """
    This is an autogenerated partial class definition of 'NuclearEnergy'
    """

    type: Optional[Any] = ["Category:OSW00fcca05152e5a99b66844586776938b"]



class BurnRate(Velocity):
    """
    This is an autogenerated partial class definition of 'BurnRate'
    """

    type: Optional[Any] = ["Category:OSWb48038c53db852e4adb4dabd954c764c"]



class RotationalStiffness(TorquePerAngle):
    """
    Rotational Stiffness is the extent to which an object resists deformation in response to an applied torque.
    """

    type: Optional[Any] = ["Category:OSW9d1ede2d23795fb1b69df7704250740e"]



class ResonanceEscapeProbabilityForFission(Dimensionless):
    """
    Fraction of fission neutrons that manage to slow down from fission to thermal energies without being absorbed.
    """

    type: Optional[Any] = ["Category:OSWfce9b748bf855dbeb74a6b35a9d2062b"]



class CenterOfGravityInTheZAxis(Length):
    """
    This is an autogenerated partial class definition of 'CenterOfGravityInTheZAxis'
    """

    type: Optional[Any] = ["Category:OSW8a36c97724bc5aa28c3049aeb0ef7d86"]



class KineticEnergy(Energy):
    """
    $\textit{Kinetic Energy}$ is the energy which a body possesses as a consequence of its motion, defined as one-half the product of its mass $m$ and the square of its speed $v$, $ \frac{1}{2} mv^{2} $. The kinetic energy per unit volume of a fluid parcel is the $ \frac{1}{2}  p v^{2}$ , where $p$ is the density and $v$ the speed of the parcel. See potential energy. For relativistic speeds the kinetic energy is given by $E_k = mc^2 - m_0 c^2$, where $c$ is the velocity of light in a vacuum, $m_0$ is the rest mass, and $m$ is the moving mass.
    """

    type: Optional[Any] = ["Category:OSW3d68ad15ab0456228c948d35e26b9dfd"]



class AmountOfSubstancePerVolume(Concentration):
    """
    The amount of substance per unit volume is called the molar density. Molar density is an intensive property of a substance and depends on the temperature and pressure.
    """

    type: Optional[Any] = ["Category:OSW98493d0d7b8b528fa42a2332c8cf502f"]



class LinearElectricCurrent(LinearElectricCurrentDensity):
    """
    "Linear Electric Linear Current" is the electric current per unit line.
    """

    type: Optional[Any] = ["Category:OSW53042a34f31b52b8a49926a2368d0e12"]



class ContractEndItemCeiSpecificationMass(Mass):
    """
    Contractual mass requirement of a delivered item. Note that The term 'control mass' is sometimes utilized as a limit in lieu of CEI mass when a CEI mass does not exist. The term 'Interface Control Document Mass' is another alternative for specifying a contractual mass requirement.
    """

    type: Optional[Any] = ["Category:OSW28dfaf74a0315d0c82f6e6faaaa25e9e"]



class WebTimeAveragePressure(Pressure):
    """
    This is an autogenerated partial class definition of 'WebTimeAveragePressure'
    """

    type: Optional[Any] = ["Category:OSWfed564d1c2845f0b9b46cc40d3edc56c"]



class LuminousFluxRatio(DimensionlessRatio):
    """
    Luminous Flux Ratio (or Relative Luminous Flux or Relative Luminous Power) is the measure of the perceived power of light. It differs from radiant flux, the measure of the total power of light emitted, in that luminous flux is adjusted to reflect the varying sensitivity of the human eye to different wavelengths of light. It is expressed as a percentage or fraction of full power.
    """

    type: Optional[Any] = ["Category:OSWbb723efad62b5aed94267ff03b896fb7"]



class LuminousExitance(LuminousFluxPerArea):
    """
    Luminous Exitance is the ratio of the luminous flux dΦ, leaving an element of the surface containing the point, by the area dA of that element. #,#Quotient aus dem Lichtstrom dΦ, der ein den Punkt enthaltendes Element der Oberfläche verlässt, und der Fläche dA dieses Elementes
    """

    type: Optional[Any] = ["Category:OSWfef30199eb315ec2ba3d9c279251ea98"]



class PositiveLength1(Length):
    """
    "NonNegativeLength" is a measure of length greater than or equal to zero.
    """

    type: Optional[Any] = ["Category:OSW04772b7915d6597fadf5b7d44f4e90a5"]


class PositiveLength(PositiveLength1):
    """
    "PositiveLength" is a measure of length strictly greater than zero.
    """

    type: Optional[Any] = ["Category:OSW238bf8ec20d05670bba32c1b44182138"]



class LiftForce(Force):
    """
    The lift force, lifting force or simply lift is the sum of all the forces on a body that force it to move perpendicular to the direction of flow.
    """

    type: Optional[Any] = ["Category:OSW640ee9c8ab965ca2ae9a83571a2e057e"]



class SpecificGibbsEnergy(SpecificEnergy):
    """
    Energy has corresponding intensive (size-independent) properties for pure materials. A corresponding intensive property is "Specific Gibbs Energy}, which is $\textit{Gibbs Energy} per mass of substance involved. $\textit{Specific Gibbs Energy" is denoted by a lower case g, with dimension of energy per mass (SI unit: joule/kg).
    """

    type: Optional[Any] = ["Category:OSW68ebaa3e9a6b5caa90f1486bd5236739"]



class RadiusOfCurvature(Length):
    """
    In geometry, the "Radius of Curvature", R, of a curve at a point is a measure of the radius of the circular arc which best approximates the curve at that point.
    """

    type: Optional[Any] = ["Category:OSWb9fc44a868dd59369128bda6e511507d"]



class Circulation(AreaPerTime):
    """
    In fluid dynamics, circulation is the line integral around a closed curve of the fluid velocity. It has dimensions of length squared over time.
    """

    type: Optional[Any] = ["Category:OSWec3279eba6a057f49cd2b5b384701930"]



class DonorIonizationEnergy(IonizationEnergy):
    """
    "Donor Ionization Energy" is the ionization energy of a donor.
    """

    type: Optional[Any] = ["Category:OSWf5c5b968f6125fab80cfdbc0a74706fa"]



class SuperconductionTransitionTemperature(Temperature):
    """
    "Superconduction Transition Temperature" is the critical thermodynamic temperature of a superconductor.
    """

    type: Optional[Any] = ["Category:OSW416ee5dc68e553579a81e352df2a0641"]



class MagnetizationField(ElectricCurrentPerLength):
    """
    The Magnetization Field is defined as the ratio of magnetic moment per unit volume. It is a vector-valued quantity.
    """

    type: Optional[Any] = ["Category:OSW656dd9cc223359e3bc88b114c9e4c231"]



class BiodegredationHalfLife(Time):
    """
    A time that quantifies how long it takes to reduce a substance's concentration by 50% from any concentration point in time in a water or soil environment by either bacteria or another living organism.
    """

    type: Optional[Any] = ["Category:OSW053f9587dee85c8b809d6ada48db67cd"]



class InitialVehicleMass(Mass):
    """
    This is an autogenerated partial class definition of 'InitialVehicleMass'
    """

    type: Optional[Any] = ["Category:OSWa573ff74e1f15ca286ce442b065146dc"]



class GapEnergy(Energy):
    """
    "Gap Energy" is the difference in energy between the lowest level of conduction band and the highest level of valence band. It is an energy range in a solid where no electron states can exist.
    """

    type: Optional[Any] = ["Category:OSW78b09fe474c85bf09529d7eb3db0fe78"]



class MacroscopicTotalCrossSection(CrossSection):
    """
    "Macroscopic Total Cross-section" is the total cross-sections for all atoms or other entities in a given 3D domain, divided by the volume of that domain.
    """

    type: Optional[Any] = ["Category:OSW2360d68f008257478577b2fa9b8facba"]



class EllipticalOrbitPerigeeVelocity(VehicleVelocity):
    """
    Velocity at apogee for an elliptical orbit velocity.
    """

    type: Optional[Any] = ["Category:OSWaabb19e4a4065b32adf894d97cb462b6"]



class MeanLifetime(Time):
    """
    The "Mean Lifetime" is the average length of time that an element remains in the set of discrete elements in a decaying quantity, $N(t)$.
    """

    type: Optional[Any] = ["Category:OSW463ab2ae42485ddca80f31dca59d3113"]



class IonizationEnergy(Energy):
    """
    "Ionization Energy" is the energy difference between an electron at rest at infinity and an electron at a certain energy level. The amount of energy required to remove an electron from that atom or molecule in the gas phase.
    """

    type: Optional[Any] = ["Category:OSW510287e6716f5be098e9ad2c80ea3d4f"]



class CenterOfGravityInTheXAxis(Length):
    """
    This is an autogenerated partial class definition of 'CenterOfGravityInTheXAxis'
    """

    type: Optional[Any] = ["Category:OSW2e463acf59d75caa99a6513b48de1b7c"]



class DryMass(Mass):
    """
    Mass of a system without the propellants, pressurants, reserve or residual fluids, personnel and personnel provisions, and cargo.
    """

    type: Optional[Any] = ["Category:OSW40c535449288505cb9bd50a76307e6fb"]



class ThermalEfficiency(DimensionlessRatio):
    """
    Thermal efficiency is a dimensionless performance measure of a thermal device such as an internal combustion engine, a boiler, or a furnace. The input to the device is heat, or the heat-content of a fuel that is consumed. The desired output is mechanical work, or heat, or possibly both.
    """

    type: Optional[Any] = ["Category:OSW809975f970ac5bb798bd97804233445e"]



class ExitPlanePressure(Pressure):
    """
    This is an autogenerated partial class definition of 'ExitPlanePressure'
    """

    type: Optional[Any] = ["Category:OSWd42f78f403bd5873b1ba3409d0816d39"]



class IonicCharge(ElectricCharge):
    """
    The total charge of an ion. The charge of an electron; the charge of any ion is equal to this electron charge in magnitude, or is an integral multiple of it.
    """

    type: Optional[Any] = ["Category:OSWb5335e62cf015a14b489876b4e6accec"]



class FermiAngularWavenumber(InverseLength):
    """
    This is an autogenerated partial class definition of 'FermiAngularWavenumber'
    """

    type: Optional[Any] = ["Category:OSW7a5bf2471b1954dba52aef0bf1a3fd28"]



class MassDelivered(Mass):
    """
    The minimum mass a propulsive system can deliver to a specified target or location. Most mass- delivered requirements have associated Delta-V requirements, effectively specifying the path between the two points.
    """

    type: Optional[Any] = ["Category:OSWa3f14dbda73f5a4faa19595388c74d3e"]



class ElectricChargeSurfaceDensity(ElectricChargePerArea):
    """
    In electromagnetism, charge density is a measure of electric charge per unit volume of space, in one, two or three dimensions. More specifically: the linear, surface, or volume charge density is the amount of electric charge per unit length, surface area, or volume, respectively.
    """

    type: Optional[Any] = ["Category:OSW373a1882b43756628a65a731497d5eee"]



class CenterOfGravityInTheYAxis(Length):
    """
    This is an autogenerated partial class definition of 'CenterOfGravityInTheYAxis'
    """

    type: Optional[Any] = ["Category:OSW6bb48a64adab53b290fecfec20f2ee3a"]



class ThermalEnergy(Energy):
    """
    "Thermal Energy" is the portion of the thermodynamic or internal energy of a system that is responsible for the temperature of the system. From a macroscopic thermodynamic description, the thermal energy of a system is given by its constant volume specific heat capacity C(T), a temperature coefficient also called thermal capacity, at any given absolute temperature (T): $U_{thermal} = C(T) \cdot T$.
    """

    type: Optional[Any] = ["Category:OSW487ed07f775b5dc2b0f8185d06e33fb8"]



class LengthForce(Work):
    """
    This is an autogenerated partial class definition of 'LengthForce'
    """

    type: Optional[Any] = ["Category:OSW34752151769754e88b1f878b2b2b7bea"]



class NuclearRadius(Length):
    """
    "Nuclear Radius" is the conventional radius of sphere in which the nuclear matter is included
    """

    type: Optional[Any] = ["Category:OSW15a0e40b150c598db6a50b85921bba29"]



class ElectricFluxDensity(ElectricChargePerArea):
    """
    $\textit{Electric Flux Density}$, also referred to as $\textit{Electric Displacement}$, is related to electric charge density by the following equation: $\text{div} \; D = \rho$, where $\text{div}$ denotes the divergence.
    """

    type: Optional[Any] = ["Category:OSW554c1d1b94535a179366575d25dc4c6b"]



class HeatCapacityRatio(DimensionlessRatio):
    """
    The heat capacity ratio, or ratio of specific heats, is the ratio of the heat capacity at constant pressure ($C_P$) to heat capacity at constant volume ($C_V$). For an ideal gas, the heat capacity is constant with temperature ($\theta$). Accordingly we can express the enthalpy as $H = C_P*\theta$ and the internal energy as $U = C_V \cdot \theta$. Thus, it can also be said that the heat capacity ratio is the ratio between enthalpy and internal energy.
    """

    type: Optional[Any] = ["Category:OSW1045cc5910ff5d9dbe61e2e68363a9bc"]



class AreicMass(MassPerArea):
    """
    This is an autogenerated partial class definition of 'AreicMass'
    """

    type: Optional[Any] = ["Category:OSW801c52067ff25e99b4c896d99f25aa06"]



class CharacteristicAcousticImpedance(AcousticImpediance):
    """
    Characteristic impedance at a point in a non-dissipative medium and for a plane progressive wave, the quotient of the sound pressure $p$ by the component of the sound particle velocity $v$ in the direction of the wave propagation.
    """

    type: Optional[Any] = ["Category:OSW8fab4f29a54f56db8cabbd1cb60b9501"]



class AngularWavenumber(InverseLength):
    """
    "wavenumber" is the spatial frequency of a wave - the number of waves that exist over a specified distance. More formally, it is the reciprocal of the wavelength. It is also the magnitude of the wave vector.
    """

    type: Optional[Any] = ["Category:OSW3672230578c1593c91fd69449f82fe93"]



class CenterOfGravityInTheZAxis(Length):
    """
    This is an autogenerated partial class definition of 'CenterOfGravityInTheZAxis'
    """

    type: Optional[Any] = ["Category:OSW0b3702d2568e5a7c8c440028bf9a7a10"]



class HeatFlowRatePerUnitArea(PowerPerArea):
    """
    $\textit{Heat Flux}$ is the heat rate per area. In SI units, heat flux is measured in $W/m^2$. Heat rate is a scalar quantity, while heat flux is a vectorial quantity. To define the heat flux at a certain point in space, one takes the limiting case where the size of the surface becomes infinitesimally small.
    """

    type: Optional[Any] = ["Category:OSWa664a34fb54f5c3c8e0422fcdd85fb27"]



class CoefficientOfPerformance(DimensionlessRatio):
    """
    ""Coefficient of Performance",is a measure of the efficiency of a heating or cooling system, defined as the ratio of useful heating or cooling output to the energy input required to achieve it.
    """

    type: Optional[Any] = ["Category:OSW9756d434853751d8aea88dfddd696a49"]



class DragForce(Force):
    """
    In fluid dynamics, drag refers to forces which act on a solid object in the direction of the relative fluid flow velocity. Unlike other resistive forces such as dry friction, which is nearly independent of velocity, drag forces depend on velocity.
    Drag forces always decrease fluid velocity relative to the solid object in the fluid's path.
    """

    type: Optional[Any] = ["Category:OSWc03790733d68543285b90a8affe46b72"]



class FlightPerformanceReservePropellantMass(Mass):
    """
    A quantity of propellant, at a nominal mixture ratio, along with fuel bias that is set aside from total propellant loaded to cover for statistical variations of flight hardware characteristics and environment conditions on the day of launch. The launch vehicle is designed to accommodate the maximum FPR loading.
    """

    type: Optional[Any] = ["Category:OSW9b95f9461de55e07a43302bc23eebc9b"]



class InternalEnergy(Energy):
    """
    The internal energy is the total energy contained by a thermodynamic system. It is the energy needed to create the system, but excludes the energy to displace the system's surroundings, any energy associated with a move as a whole, or due to external force fields. Internal energy has two major components, kinetic energy and potential energy. The internal energy (U) is the sum of all forms of energy (Ei) intrinsic to a thermodynamic system:  $  U = \sum_i E_i $
    """

    type: Optional[Any] = ["Category:OSWa1400ee0d19b55c09bfac6fad4965a58"]



class PathLength(Length):
    """
    "PathLength" is
    """

    type: Optional[Any] = ["Category:OSW00ae7010dd635404bd82873cfd7a3254"]



class DiffusionCoefficientForFluenceRate(Length):
    """
    The "Diffusion Coefficient for Fluence Rate" is a proportionality constant between the .
    """

    type: Optional[Any] = ["Category:OSWfadb71c303c55656bd54245387aa2ca8"]



class LondonPenetrationDepth(Length):
    """
    "London Penetration Depth" characterizes the distance to which a magnetic field penetrates into a superconductor and becomes equal to 1/e times that of the magnetic field at the surface of the superconductor.
    """

    type: Optional[Any] = ["Category:OSW956f71432fec58ba8d84b3744876ad5d"]



class SoilAdsorptionCoefficient(SpecificVolume):
    """
    A specific volume that is the ratio of the amount of substance adsorbed per unit weight of organic carbon in the soil or sediment to the concentration of the chemical in aqueous solution at equilibrium.
    """

    type: Optional[Any] = ["Category:OSW8a3a8be1f11953c5bb43a0d6ae3efac2"]



class Weight(Force):
    """
    The force with which a body is attracted toward an astronomical body.  Or, the product of the mass of a body and the acceleration acting on a body.  In a dynamic situation, the weight can be a multiple of that under resting conditions. Weight also varies on other planets in accordance with their gravity.
    """

    type: Optional[Any] = ["Category:OSW0ed75cfa55dc55adbbbecbf4e22744c0"]



class StructuralEfficiency(Dimensionless):
    """
    Structural efficiency is a function of the weight of structure to the afforded vehicle's strength.
    """

    type: Optional[Any] = ["Category:OSW5ba1cba5d9005434a6f280a50b462591"]



class CompressibilityFactor(DimensionlessRatio):
    """
    The compressibility factor ($Z$) is a useful thermodynamic property for modifying the ideal gas law to account for the real gas behaviour. The closer a gas is to a phase change, the larger the deviations from ideal behavior. It is simply defined as the ratio of the molar volume of a gas to the molar volume of an ideal gas at the same temperature and pressure. Values for compressibility are calculated using equations of state (EOS), such as the virial equation and van der Waals equation. The compressibility factor for specific gases can be obtained, with out calculation, from compressibility charts. These charts are created by plotting Z as a function of pressure at constant temperature.
    """

    type: Optional[Any] = ["Category:OSW818055ce036f5845a326d24ddba849eb"]



class CO2Equivalent(MassEquivalent):
    """
    The CO2 equivalent is a measure used to compare the emissions from various greenhouse gases
      on the basis of their global-warming potential (GWP), by converting amounts of other gases to the equivalent amount
      of carbon dioxide with the same global warming potential.
    """

    type: Optional[Any] = ["Category:OSW3ba3f32bc07955f3a522c8159c29a279"]



class AtomicEnergy(Energy):
    """
    skalare Größe von Elementarteilchen, die bei beliebiger Umwandlung innerhalb eines Systems erhalten bleibt und als gespeichertes Arbeitsvermögen die Fähigkeit eines physikalischen Systems darstellt, Arbeit zu verrichten
    """

    type: Optional[Any] = ["Category:OSW8d4a387a6b1d5ed7849485215602a553"]



class IonConcentration(Concentration):
    """
    "Ion Concentration" is the moles of ions per volume of solution.
    """

    type: Optional[Any] = ["Category:OSWc0f9f761f30d5a1baf90b44ed6eef37d"]



class FishBiotransformationHalfLife(Time):
    """
    A time that quantifies how long its takes to transform 50% of a substance's total concentration from any concentration point in time in fish via whole body metabolic reactions.
    """

    type: Optional[Any] = ["Category:OSWf75817e6c9af5ba9b9d3ed582403f82c"]



class RadialDistance(Length):
    """
    In classical geometry, the "Radial Distance" is a coordinate in polar coordinate systems (r, $\theta$). Basically the radial distance is the scalar Euclidean distance between a point and the origin of the system of coordinates.
    """

    type: Optional[Any] = ["Category:OSW1c582dc8159751f99cb83fa8f973389b"]



class DimensionlessRatio(Dimensionless):
    """
    This is an autogenerated partial class definition of 'DimensionlessRatio'
    """

    type: Optional[Any] = ["Category:OSW67faac860ed758758aa4484387e5d5c9"]



class FissionCoreRadiusToHeightRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'FissionCoreRadiusToHeightRatio'
    """

    type: Optional[Any] = ["Category:OSW58245ed6bf6f515db05601290b82c811"]



class Thrust(Force):
    """
    Thrust is a reaction force described quantitatively by Newton's Second and Third Laws. When a system expels or accelerates mass in one direction the accelerated mass will cause a proportional but opposite force on that system.
    """

    type: Optional[Any] = ["Category:OSW7bf742d673495bb8bd77d1ea5295b2cd"]



class Radiosity(PowerPerArea):
    """
    Radiosity is the total emitted and reflected radiation leaving a surface.
    """

    type: Optional[Any] = ["Category:OSW2c869e5a09fa5fdfb818543b40bacb08"]



class MolalityOfSolute(AmountOfSubstancePerMass):
    """
    The "Molality of Solute" of a solution is defined as the amount of substance of solute divided by the mass in kg of the solvent.
    """

    type: Optional[Any] = ["Category:OSW4041cc5b57dc5efcbb9701f04e4a68ce"]



class FlightPathAngle(Angle):
    """
    Flight path angle is defined in two different ways. To the aerodynamicist, it is the angle between the flight path vector (where the airplane is going) and the local atmosphere. To the flight crew, it is normally known as the angle between the flight path vector and the horizon, also known as the climb (or descent) angle.
    """

    type: Optional[Any] = ["Category:OSW00c10a2500cf59fdbfaf48764629b35d"]



class FissionFuelUtilizationFactor(Dimensionless):
    """
    This is an autogenerated partial class definition of 'FissionFuelUtilizationFactor'
    """

    type: Optional[Any] = ["Category:OSWc11d565a6b4950c9be08c3ba7b9a106c"]



class SlowingDownLength(Length):
    """
    "Slowing-Down Length" is the average straight-line distance that a fast neutron will travel between its introduction into the slowing-downmedium (moderator) and thermalization.
    """

    type: Optional[Any] = ["Category:OSWcabedf8597d25a3eb8d196f2b864e0a6"]



class ActionTime(Time):
    """
    This is an autogenerated partial class definition of 'ActionTime'
    """

    type: Optional[Any] = ["Category:OSWd3e857a0417758e482950553327802dc"]



class Breadth(Length):
    """
    "Breadth" is the extent or measure of how broad or wide something is.
    """

    type: Optional[Any] = ["Category:OSWc2d5b706ce5550b79cb2d73ad8f91acd"]



class MassGrowthAllowance(Mass):
    """
    A factor applied to basic mass at the lowest level of design detail available based on type and maturity of hardware according to an approved MGA depletion schedule.
    """

    type: Optional[Any] = ["Category:OSW61e1f096ca895a01b3f540bd78a0c78c"]



class MigrationLength(Length):
    """
    "Migration Length" is the square root of the migration area.
    """

    type: Optional[Any] = ["Category:OSW4fe6cc8e0eb65db889f4b790342383cb"]



class Wavenumber(InverseLength):
    """
    "Wavenumber" is the spatial frequency of a wave - the number of waves that exist over a specified distance. More formally, it is the reciprocal of the wavelength. It is also the magnitude of the wave vector. Light passing through different media keeps its frequency, but not its wavelength or wavenumber. The unit for wavenumber commonly used in spectroscopy is centimetre to power minus one, PER-CM, rather than metre to power minus one, PER-M.
    """

    type: Optional[Any] = ["Category:OSW0bca40ca00e05ec4aab8e33e1a4acf8f"]



class MaximumBetaParticleEnergy(Energy):
    """
    "Maximum Beta-Particle Energy" is the maximum energy of the energy spectrum in a beta-particle disintegration process.
    """

    type: Optional[Any] = ["Category:OSW69b54fc65f1d506eb15053de18dc035e"]



class MoleFraction(DimensionlessRatio):
    """
    In chemistry, the mole fraction of a component in a mixture is the relative proportion of molecules belonging to the component to those in the mixture, by number of molecules. It is one way of measuring concentration.
    """

    type: Optional[Any] = ["Category:OSW75c0b290d1a451fb8de36ffa84bdc59c"]



class DoseEquivalent(SpecificEnergy):
    """
    "Dose Equivalent" (former), or $\textit{Equivalent Absorbed Radiation Dose}$, usually shortened to $\textit{Equivalent Dose}$, is a computed average measure of the radiation absorbed by a fixed mass of biological tissue, that attempts to account for the different biological damage potential of different types of ionizing radiation. The equivalent dose to a tissue is found by multiplying the absorbed dose, in gray, by a dimensionless "quality factor" $Q$, dependent upon radiation type, and by another dimensionless factor $N$, dependent on all other pertinent factors. N depends upon the part of the body irradiated, the time and volume over which the dose was spread, even the species of the subject.
    """

    type: Optional[Any] = ["Category:OSWfe1ff8f44b165f1f985b575117e59d3b"]



class Diameter(Length):
    """
    In classical geometry, the "Diameter" of a circle is any straight line segment that passes through the center of the circle and whose endpoints lie on the circle.
    """

    type: Optional[Any] = ["Category:OSW24275b1c56ea58dcae38c44409251a64"]



class FailureRate(Incidence):
    """
    Grenzwert - falls er existiert - des Quotienten aus der bedingten Wahrscheinlichkeit, dass der Ausfallzeitpunkt t eines Betriebsmittels in ein gegebenes Zeitintervall (t, t + Δt) fällt, und der Dauer dieses Zeitintervalls, wenn Δt gegen null geht und das Betriebsmittel sich zu Beginn des Zeitintervalls im betriebsfähigen Zustand befindet
    """

    type: Optional[Any] = ["Category:OSW11d1e28ece2152e3868f438d4eb40a11"]



class BoilingPointTemperature(Temperature):
    """
    A temperature that is the one at which a substance will change its physical state from a liquid to a gas.  It is also the temperature where the liquid and gaseous forms of a pure substance can exist in equilibrium.
    """

    type: Optional[Any] = ["Category:OSW2ab56dc7ae315aa98995de458930f379"]



class MassNumber(Count):
    """
    The "Mass Number" (A), also called atomic mass number or nucleon number, is the total number of protons and neutrons (together known as nucleons) in an atomic nucleus. Nuclides with the same value of $A$ are called isobars.
    """

    type: Optional[Any] = ["Category:OSW57d546ae6cae5831a7efd0cf3b933b27"]



class ChargeNumber(Dimensionless):
    """
    The "Charge Number", or just valance of an ion is the coefficient that, when multiplied by the elementary charge, gives the ion's charge.
    """

    type: Optional[Any] = ["Category:OSW0accaf0456ef52ee88161e974f36e3ba"]



class CarrierLifetime(Time):
    """
    "Carrier LifetIme" is a time constant for recombination or trapping of minority charge carriers in semiconductors.
    """

    type: Optional[Any] = ["Category:OSWd4dba64e4ce95ba49505900a3b92d2d2"]



class PhononMeanFreePath(Length):
    """
    "Phonon Mean Free Path" is the mean free path of phonons.
    """

    type: Optional[Any] = ["Category:OSW05ead50111145f24adcfe86c6645c303"]



class DensityOfTheExhaustGases(Density):
    """
    This is an autogenerated partial class definition of 'DensityOfTheExhaustGases'
    """

    type: Optional[Any] = ["Category:OSW0ae584a5bdf95705a72f864c11e61486"]



class CubicExpansionCoefficient(ExpansionRatio):
    """
    This is an autogenerated partial class definition of 'CubicExpansionCoefficient'
    """

    type: Optional[Any] = ["Category:OSW7462160259c65b45be6369b78ee192aa"]



class Enthalpy(Energy):
    """
    In thermodynamics, $\textit{enthalpy}$ is the sum of the internal energy $U$ and the product of pressure $p$ and volume $V$ of a system. The characteristic function (also known as thermodynamic potential) $\textit{enthalpy}$ used to be called $\textit{heat content}$, which is why it is conventionally indicated by $H$. The specific enthalpy of a working mass is a property of that mass used in thermodynamics, defined as $h=u+p \cdot v$,  where $u$ is the specific internal energy, $p$ is the pressure, and $v$ is specific volume. In other words, $h = H / m$ where $m$ is the mass of the system. The SI unit for $\textit{Specific Enthalpy}$ is $\textit{joules per kilogram}$
    """

    type: Optional[Any] = ["Category:OSW877daca6abe55171adc9c6f0ae1ac011"]



class CoherenceLength(Length):
    """
    "Coherence Length" characterizes the distance in a superconductor over which the effect of a perturbation is appreciable.
    """

    type: Optional[Any] = ["Category:OSW4fdc07e10e3554b4a1bfec197dab94ba"]



class Width(Length):
    """
    "Width" is the middle of three dimensions: length, width, thickness.
    """

    type: Optional[Any] = ["Category:OSWf8e8296734a759deb817315f69a78fb9"]



class QuantumNumber(Dimensionless):
    """
    The "Quantum Number" describes values of conserved quantities in the dynamics of the quantum system. Perhaps the most peculiar aspect of quantum mechanics is the quantization of observable quantities, since quantum numbers are discrete sets of integers or half-integers.
    """

    type: Optional[Any] = ["Category:OSWa35c06b30b7750c49dd53768ffd9e756"]



class RadiantFlux(Power):
    """
    Radiant Flux, or radiant power, is the measure of the total power of electromagnetic radiation (including infrared, ultraviolet, and visible light). The power may be the total emitted from a source, or the total landing on a particular surface.
    """

    type: Optional[Any] = ["Category:OSW91a9f32b98cb5dc39ad2c3b039d86ba7"]



class FundamentalReciprocalLatticeVector(AngularReciprocalLatticeVector):
    """
    "Fundamental Reciprocal Lattice Vector" are fundamental, or primary, translation vectors the reciprocal lattice.
    """

    type: Optional[Any] = ["Category:OSWdb0431d4d0ea5820a7838ea18c8e04af"]



class OsmoticPressure(Pressure):
    """
    The "Osmotic Pressure" is the pressure which needs to be applied to a solution to prevent the inward flow of water across a semipermeable membrane.
    """

    type: Optional[Any] = ["Category:OSWa76a1a2e60f952fd9b4bda2edfd4047a"]



class AngleOfAttack(Angle):
    """
    Angle of attack  is the angle between the oncoming air or relative wind and a reference line on the airplane or wing.
    """

    type: Optional[Any] = ["Category:OSW1d2dc89443765cf8935b61016cbe5bd1"]



class FuelBias(Dimensionless):
    """
    An additional quantity of fuel to ensure depletion of high-weight oxidizer before fuel for systems with high-oxidizer mixing ratios (e.g., 6:1). This practice allows for more efficient propellant utilization. Denoted as a percentage.
    """

    type: Optional[Any] = ["Category:OSWb56889844bf25ea99847d1c56e9e8042"]



class Piece(Count):
    """
    This is an autogenerated partial class definition of 'Piece'
    """

    type: Optional[Any] = ["Category:OSWdc14ddb70b105a98bfa6afc265622908"]



class Friction(Force):
    """
    "Friction" is the force of two surfaces In contact, or the force of a medium acting on a moving object (that is air on an aircraft). When contacting surfaces move relative to each other, the friction between the two objects converts kinetic energy into thermal energy.
    """

    type: Optional[Any] = ["Category:OSW92473183e45854a8bd13de8f0aefff19"]



class Altitude(Length):
    """
    Altitude or height is defined based on the context in which it is used (aviation, geometry, geographical survey, sport, and more). As a general definition, altitude is a distance measurement, usually in the vertical or "up" direction, between a reference datum and a point or object. The reference datum also often varies according to the context. [Wikipedia]
    """

    type: Optional[Any] = ["Category:OSW2423ce4a8e5c5a2782492fd72d06ee04"]



class Heat(ThermalEnergy):
    """
    "Heat" is the energy transferred by a thermal process.  Heat can be measured in terms of the dynamical units of energy, as the erg, joule, etc., or in terms of the amount of energy required to produce a definite thermal change in some substance, as, for example, the energy required per degree to raise the temperature of a unit mass of water at some temperature ( calorie, Btu).
    """

    type: Optional[Any] = ["Category:OSWcba88507fe875a5fbebc2a29a5691f03"]



class Gain(DimensionlessRatio):
    """
    A general term used to denote an increase in signal power or signal strength in transmission from one point to another. Gain is usually expressed in decibels and is widely used to denote transducer gain.  An increase or amplification. In radar there are two general usages of the term: (a) antenna gain, or gain factor, is the ratio of the power transmitted along the beam axis to that of an isotropic radiator transmitting the same total power; (b) receiver gain, or video gain, is the amplification given a signal by the receiver.
    """

    type: Optional[Any] = ["Category:OSW064063da72515522948cf03fca30ebbc"]



class PositiveDimensionlessRatio(DimensionlessRatio):
    """
    A "Normalized Dimensionless Ratio" is a dimensionless ratio ranging from 0.0 to 1.0
    """

    type: Optional[Any] = ["Category:OSWa76d21440d01543aaa63a7e8d97c0438"]



class DryBulbTemperature(Temperature):
    """
    The temperature of air measured by a thermometer freely exposed to the air, but shielded from radiation.
    """

    type: Optional[Any] = ["Category:OSWfde09f3b6e9b5c2f947f1e1bdb12f20e"]



class InformationEntropy(Dimensionless):
    """
    Information Entropy is a concept from information theory. It tells how much information there is in an event. In general, the more uncertain or random the event is, the more information it will contain. The concept of information entropy was created by a mathematician. He was named Claude Elwood Shannon. It has applications in many areas, including lossless data compression, statistical inference, cryptography and recently in other disciplines as biology, physics or machine learning.
    """

    type: Optional[Any] = ["Category:OSW9b6dead1d47358a099b73ba6b309597e"]



class TrueExhaustVelocity(Velocity):
    """
    This is an autogenerated partial class definition of 'TrueExhaustVelocity'
    """

    type: Optional[Any] = ["Category:OSW1397ec6562ae5659b527a5d3738756c7"]



class PotentialEnergy(Energy):
    """
    Energy possessed by a body by virtue of its position in a gravity field in contrast with kinetic energy, that possessed by virtue of its motion.
    """

    type: Optional[Any] = ["Category:OSW0dbd1a690ea0550cb83bac795f460fa6"]



class AverageEnergyLossPerElementaryChargeProduced(Energy):
    """
    "Average Energy Loss per Elementary Charge Produced" is also referred to as average energy loss per ion pair formed.
    """

    type: Optional[Any] = ["Category:OSW297cbb81c60a534a885218aaa3caeb0f"]



class DiastolicBloodPressure(Pressure):
    """
    The pressure of blood in the arteries which rises to a maximum as blood is pumped out by the left ventricle (systole) and drops to a minimum in diastole. The systolic/diastolic pressure is normally ~120/80 mmHg in a young adult.
    """

    type: Optional[Any] = ["Category:OSW9426aa0e1345513a8a8ee97bdd841800"]



class ExhaustGasesSpecificHeat(SpecificHeatCapacity):
    """
    Specific heat of exhaust gases at constant pressure.
    """

    type: Optional[Any] = ["Category:OSW2435e3d417be54418892bf902cfc939a"]



class PropellantTemperature(Temperature):
    """
    This is an autogenerated partial class definition of 'PropellantTemperature'
    """

    type: Optional[Any] = ["Category:OSWa78a937a78d65bf89d04af65b0ae5b4a"]



class ShearStrain(Strain):
    """
    Shear Strain is the amount of deformation perpendicular to a given line rather than parallel to it.
    """

    type: Optional[Any] = ["Category:OSWcd5753abfaf35c2992b9887c20e8443c"]



class ModulusOfRotationalSubgradeReaction(ForcePerAngle):
    """
    Modulus of Rotational Subgrade Reaction is a measure for modulus of rotational subgrade reaction, which expresses the rotational elastic bedding of a linear structural element per length, such as for a beam. It is typically measured in Nm/(m*rad).
    """

    type: Optional[Any] = ["Category:OSW58c6699731405450935765efe8e170d5"]



class MassExcess(Mass):
    """
    The "Mass Excess" of a nuclide is the difference between its actual mass and its mass number in atomic mass units. It is one of the predominant methods for tabulating nuclear mass.
    """

    type: Optional[Any] = ["Category:OSW845f46b0b81c5e1e985b0532aa2428d6"]



class PositivePlaneAngle(PlaneAngle):
    """
    A "PositivePlaneAngle" is a plane angle strictly greater than zero.
    """

    type: Optional[Any] = ["Category:OSW84aa24df02cb576ab92fda7f55dcac6e"]



class LengthRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'LengthRatio'
    """

    type: Optional[Any] = ["Category:OSW031793bb135f5bab91e46bbf96621f93"]


class LinearStrain(LengthRatio):
    """
    A strain is a normalized measure of deformation representing the displacement between particles in the body relative to a reference length.
    """

    type: Optional[Any] = ["Category:OSW0c6e03c01296556aba2d7ac65750357e"]



class Thickness(Length):
    """
    "Thickness" is the the smallest of three dimensions: length, width, thickness.
    """

    type: Optional[Any] = ["Category:OSWd34599c980285400b402962f7a36cc44"]



class ChemicalPotential(MolarEnergy):
    """
    "Chemical Potential", also known as partial molar free energy, is a form of potential energy that can be absorbed or released during a chemical reaction.
    """

    type: Optional[Any] = ["Category:OSW7119e1d761815d4facb1dbee71829517"]



class FundamentalLatticeVector(LatticeVector):
    """
    "Fundamental Lattice vector" are fundamental translation vectors for the crystal lattice.
    """

    type: Optional[Any] = ["Category:OSWcf6c6cffa49b53ff80cfd4cb418b3be5"]



class IonTransportNumber(DimensionlessRatio):
    """
    The "Ion Transport Number" is a quantity which indicates the different contribution of ions to the electric current in electrolytes due to different electrical mobility.
    """

    type: Optional[Any] = ["Category:OSW4b7775a17ff1520aaad9af4ddb1f283c"]



class CenterOfMassCom(PositionVector):
    """
    The point at which the distributed mass of a composite body can be acted upon by a force without inducing any rotation of the composite body.
    """

    type: Optional[Any] = ["Category:OSW55d3f263afd753388c3dd35e1e5d8481"]



class AtomicCharge(ElectricCharge):
    """
    The electric charge of an ion, equal to the number of electrons the atom has gained or lost in its ionization multiplied by the charge on one electron.
    """

    type: Optional[Any] = ["Category:OSWb3de57b2dac651aaa2f72a50ded04fb2"]



class DynamicFriction(Friction):
    """
    Kinetic (or dynamic) friction occurs when two objects are moving relative to each other and rub together (like a sled on the ground).
    """

    type: Optional[Any] = ["Category:OSW77c9caa170e1512a94534c634ef1545e"]



class RelaxationTime(Time):
    """
    "Relaxation TIme" is a time constant for exponential decay towards equilibrium.
    """

    type: Optional[Any] = ["Category:OSW63d2744b144252eca7795fec18656d3f"]



class SoundIntensity(PowerPerArea):
    """
    Sound intensity or acoustic intensity ($I$) is defined as the sound power $P_a$ per unit area $A$. The usual context is the noise measurement of sound intensity in the air at a listener's location as a sound energy quantity.
    """

    type: Optional[Any] = ["Category:OSW7450be7f3aa3552e9da4bb8a6d952f9f"]



class CalorificValue(SpecificEnergy):
    """
    The heating value (or energy value or calorific value) of a substance, usually a fuel or food (see food energy), is the amount of heat released during the combustion of a specified amount of it.
    """

    type: Optional[Any] = ["Category:OSWa88820451d0e5563927cef63406f97ab"]



class Height(Length):
    """
    "Height" is the measurement of vertical distance, but has two meanings in common use. It can either indicate how "tall" something is, or how "high up" it is.
    """

    type: Optional[Any] = ["Category:OSWc1bdd6bcfc955882ba1d068110ae41cc"]



class DisplacementVectorOfIon(Length):
    """
    "Displacement Vector of Ion" is the .
    """

    type: Optional[Any] = ["Category:OSWee57e9ea6fbe580a83765aa62cafed15"]



class ShearStress(Stress):
    """
    Shear stress occurs when the force  occurs in shear, or perpendicular to the normal.
    """

    type: Optional[Any] = ["Category:OSWf0ab9cfde91f5e7a8b21de948729e1ac"]



class DutyCycle(DimensionlessRatio):
    """
    A duty cycle or power cycle is the fraction of one period in which a signal or system is active.
    """

    type: Optional[Any] = ["Category:OSW0ddf63f69e725cb69e0e5e0deca608b2"]



class MeltingPointTemperature(Temperature):
    """
    A temperature that is the one at which a substance will change its physical state from a solid to a liquid.  It is also the temperature where the solid and liquid forms of a pure substance can exist in equilibrium.
    """

    type: Optional[Any] = ["Category:OSW3dc44dc69cfb5c34a37543b3c7bf7017"]



class RelativeMassDefect(DimensionlessRatio):
    """
    The "Relative Mass Defect" is the mass defect between the monoisotopic mass of an element and the mass of its A + 1 or its A + 2 isotopic cluster.
    """

    type: Optional[Any] = ["Category:OSWd648b91cc3585f4cb1299ebb6b148dc4"]



class SpecificInternalEnergy(SpecificEnergy):
    """
    Energy has corresponding intensive (size-independent) properties for pure materials. A corresponding intensive property is specific internal energy, which is energy per mass of substance involved. Specific internal energy is denoted by a lower case u, with dimension of energy per mass (SI unit: joule/kg).
    """

    type: Optional[Any] = ["Category:OSWaff5b15f9ff3598ea65071f64badcb81"]



class ThrustToWeightRatio(DimensionlessRatio):
    """
    Thrust-to-weight ratio is a ratio of thrust to weight of a rocket, jet engine, propeller engine, or a vehicle propelled by such an engine. It is a dimensionless quantity and is an indicator of the performance of the engine or vehicle.
    """

    type: Optional[Any] = ["Category:OSW4ca14f3ca53f54189c9a11f750f429e7"]



class KineticEnergy(Energy):
    """
    The kinetic energy of an object is the energy which it possesses due to its motion. It is defined as the work needed to accelerate a body of a given mass from rest to its stated velocity.
    """

    type: Optional[Any] = ["Category:OSWa572282dc5c4510399eeafa0ce8e8519"]



class EffectiveMass(Mass):
    """
    "Effective Mass" is used in the motional equation for electrons in solid state bodies, depending on the wavenumber and corresponding to its velocity and energy level.
    """

    type: Optional[Any] = ["Category:OSW4a5b46b736755f22ab06881a142f62e6"]



class MassPropertyUncertainty(Mass):
    """
    Variation in predicted MP due to lack of definition, manufacturing variations, environment effects, or accuracy limitation of measuring devices.
    """

    type: Optional[Any] = ["Category:OSW3a06c181a5375b68b002f7a28ff862d0"]



class ReactionEnergy(Energy):
    """
    "Reaction Energy" in a nuclear reaction, is the sum of the kinetic energies and photon energies of the reaction products minus the sum of the kinetic and photon energies of the reactants.
    """

    type: Optional[Any] = ["Category:OSWfb81293480935fe7954a0a6c341d8b9f"]



class RadiantExposure(EnergyPerArea):
    """
    Radiant exposure is a measure of the total radiant energy incident on a surface per unit area; equal to the integral over time of the radiant flux density. Also known as exposure.
    """

    type: Optional[Any] = ["Category:OSWdb037d62fb0c52948d5944b910ec7e40"]



class StochasticProcess(Frequency):
    """
    In probability theory, a stochastic process, or sometimes random process  is a collection of random variables; this is often used to represent the evolution of some random value, or system, over time. This is the probabilistic counterpart to a deterministic process (or deterministic system).
    """

    type: Optional[Any] = ["Category:OSWbec1168058375097b6157eb8ac35eab4"]



class MaximumExpectedOperatingPressure(Pressure):
    """
    This is an autogenerated partial class definition of 'MaximumExpectedOperatingPressure'
    """

    type: Optional[Any] = ["Category:OSWb9a0d2848bdf58a0b25881447ff8513d"]



class PropellantMass(Mass):
    """
    This is an autogenerated partial class definition of 'PropellantMass'
    """

    type: Optional[Any] = ["Category:OSW3cca82ea6a345bc79d209236e827ea73"]



class RadiantFluenceRate(PowerPerArea):
    """
    Radiant fluence rate, or spherical irradiance, is equal to the total radiant flux incident on a small sphere divided by the area of the diametrical cross-section of the sphere.
    """

    type: Optional[Any] = ["Category:OSW629f785658c254b1a8c69f548916443b"]



class RelativePartialPressure(PressureRatio):
    """
    This is an autogenerated partial class definition of 'RelativePartialPressure'
    """

    type: Optional[Any] = ["Category:OSW99edcb0bac12560fa33d6af42aecad67"]



class LengthRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'LengthRatio'
    """

    type: Optional[Any] = ["Category:OSW031793bb135f5bab91e46bbf96621f93"]



class Reflectance(DimensionlessRatio):
    """
    Reflectance generally refers to the fraction of incident power that is reflected at an interface, while the term "reflection coefficient" is used for the fraction of electric field reflected. Reflectance is always a real number between zero and 1.0.
    """

    type: Optional[Any] = ["Category:OSWe5e3a7fe15ab5beaa32db082ed17e1d5"]



class PositiveDimensionlessRatio(DimensionlessRatio):
    """
    A "Positive Dimensionless Ratio" is a dimensionless ratio that is greater than zero
    """

    type: Optional[Any] = ["Category:OSW49b7ea6a747e573284e9925d1d3b3b0f"]



class VoltageRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'VoltageRatio'
    """

    type: Optional[Any] = ["Category:OSWb62313a0be8e52489be495eea7c6f856"]



class VolumeStrain(Strain):
    """
    Volume, or volumetric, Strain, or dilatation (the relative variation of the volume) is the trace of the tensor $\vartheta$.
    """

    type: Optional[Any] = ["Category:OSW14e89dbad13a5ae081bffbd4dc8641a6"]



class StageStructureMass(Mass):
    """
    This is an autogenerated partial class definition of 'StageStructureMass'
    """

    type: Optional[Any] = ["Category:OSWc74bc7a7558c5c9aa7aa0282ab29e3cd"]



class FinalOrCurrentVehicleMass(Mass):
    """
    This is an autogenerated partial class definition of 'FinalOrCurrentVehicleMass'
    """

    type: Optional[Any] = ["Category:OSWa6c948d5809e504cab9fa3aae14ad79a"]



class PositiveLength(Length):
    """
    "NonNegativeLength" is a measure of length greater than or equal to zero.
    """

    type: Optional[Any] = ["Category:OSW04772b7915d6597fadf5b7d44f4e90a5"]



class SlowingDownArea(Area):
    """
    "Slowing-Down Area" in an infinite homogenous medium, is one-sixth of the mean square distance between the neutron source and the point where a neutron reaches a given energy.
    """

    type: Optional[Any] = ["Category:OSW3bb93168722e5893b632cd3889967bf0"]



class RadiantEmmitance(PowerPerArea):
    """
    Irradiance and Radiant Emittance are radiometry terms for the power per unit area of electromagnetic radiation at a surface. "Irradiance" is used when the electromagnetic radiation is incident on the surface. "Radiant emmitance" (or "radiant exitance") is used when the radiation is emerging from the surface.
    """

    type: Optional[Any] = ["Category:OSW7b7e0f4f719f5ea0a5c3ecb46749a661"]



class AtomicMass(Mass):
    """
    The "Atomic Mass" is the mass of a specific isotope, most often expressed in unified atomic mass units.
    """

    type: Optional[Any] = ["Category:OSWba53f057665b5a808021878a5dca9b99"]



class CorrelatedColourTemperature(ThermodynamicTemperature):
    """
    Correlated color temperature (CCT) is a measure of light source color appearance defined by the proximity of the light source's chromaticity coordinates to the blackbody locus, as a single number rather than the two required to specify a chromaticity.
    """

    type: Optional[Any] = ["Category:OSWaebde3cc25da54f7868f8c09f8c22336"]



class Displacement(Length):
    """
    "Displacement" is the shortest distance from the initial to the final position of a point P.
    """

    type: Optional[Any] = ["Category:OSW22c5c9fd1072518ca4e36301f8459bc8"]



class ForceMagnitude(Force):
    """
    The 'magnitude' of a force is its 'size' or 'strength', regardless of the direction in which it acts.
    """

    type: Optional[Any] = ["Category:OSW4f80d4743b2f5971bdcffe28391fa016"]


class Tension(ForceMagnitude):
    """
    This is an autogenerated partial class definition of 'Tension'
    """

    type: Optional[Any] = ["Category:OSW4874b6ee8d7b5f65a7fe5868c48fa956"]



class DynamicPressure(Pressure):
    """
    Dynamic Pressure (indicated with q, or Q, and sometimes called velocity pressure) is the quantity defined by: $q = 1/2 * \rho v^{2}$, where (using SI units),  $q$ is dynamic pressure in $pascals$, $\rho$ is fluid density in $kg/m^{3}$ (for example, density of air) and $v $ is fluid velocity in $m/s$.
    """

    type: Optional[Any] = ["Category:OSW1c2803e14f6658d7a4524335a0310023"]



class ElectronRadius(Length):
    """
    "Electron Radius", also known as the Lorentz radius or the Thomson scattering length, is based on a classical (i.e., non-quantum) relativistic model of the electron.
    """

    type: Optional[Any] = ["Category:OSW7e89dce662b353eeaa53eb5ae4ca4eb4"]



class Volume1(QuantityValue):
    """
    The volume of a solid object is the three-dimensional concept of how much space it occupies, often quantified numerically. One-dimensional figures (such as lines) and two-dimensional shapes (such as squares) are assigned zero volume in the three-dimensional space.
    """

    type: Optional[Any] = ["Category:OSWf5c54cd70ddf5ff3b1ef1aee6ae8f0cb"]
    unit: Optional[VolumeUnit] = Field(VolumeUnit.meter_cubed, title="VolumeUnit")


class Volume(Volume1):
    """
    "Volume" is the quantity of three-dimensional space enclosed by some closed boundary, for example, the space that a substance (solid, liquid, gas, or plasma) or shape occupies or contains.
    """

    type: Optional[Any] = ["Category:OSWfed64b810634552bb200c195ab1017be"]



class SpecificHelmholtzEnergy(SpecificEnergy):
    """
    $\textit{Specific Helmholtz Energy}$ is a "corresponding intensive property",
        which is $\textit{Helmholz Energy}$ per mass of substance involved.
      Energy has corresponding intensive (size-independent) properties for pure materials.
      $\textit{Specific Helmholz Energy}$ is denoted by a lower case $u$,
       with dimension of energy per mass (SI unit: $joule/kg$).
    """

    type: Optional[Any] = ["Category:OSWc9afe66910a35665b674df1fa788f6c0"]



class Incidence(Frequency):
    """
    In epidemiology, incidence is a measure of the probability of occurrence of a given medical condition in a population within a specified period of time.
    """

    type: Optional[Any] = ["Category:OSWe8d1194aeb2e5b9f877867eab5c9cae9"]



class ForceMagnitude(Force):
    """
    The 'magnitude' of a force is its 'size' or 'strength', regardless of the direction in which it acts.
    """

    type: Optional[Any] = ["Category:OSW4f80d4743b2f5971bdcffe28391fa016"]



class LossAngle(Angle):
    """
    This is an autogenerated partial class definition of 'LossAngle'
    """

    type: Optional[Any] = ["Category:OSW3045ff9460da5f55bdfb935f7996e4b3"]



class MassDefect(Mass):
    """
    The "Mass Defect", also termed mass deficit, or mass packing fraction, describes mass change (decrease) in bound systems, particularly atomic nuclei.
    """

    type: Optional[Any] = ["Category:OSW98b06c550c595e78a13ff79969b21e2e"]



class SourceVoltage(Voltage):
    """
    The quantity kind $\textit{Source Voltage}$, also referred to as $\textit{Source Tension}$
       is the voltage between the two terminals of a voltage source when there is no electric current through the source.
      The name $\text{electromotive force}$ with the abbreviation $\textit{EMF}$ and the symbol $E$ is deprecated.
    """

    type: Optional[Any] = ["Category:OSWca26a95f432052f3b6e14fddf13e7fe7"]



class CrossSectionalArea(Area):
    """
    This is an autogenerated partial class definition of 'CrossSectionalArea'
    """

    type: Optional[Any] = ["Category:OSWfcfbe2c7988950daa7b997215ad2bd60"]



class LinkedFlux(MagneticFlux):
    """
    "Linked Flux" is defined as the path integral of the magnetic vector potential. This is the line integral of a magnetic vector potential $A$ along a curve $C$. The line vector element $dr$ is the differential of position vector $r$.
    """

    type: Optional[Any] = ["Category:OSWca710662e2c35883810a8192a8113f0c"]



class ChemicalConsumptionPerMass(SpecificVolume):
    """
    In the context of a chemical durability test, this is measure of how much of a solution (often a corrosive or reactive one) is consumed or used up per unit mass of a material being tested. In other words, this the volume of solution needed to cause a certain level of chemical reaction or damage to a given mass of the material.
    """

    type: Optional[Any] = ["Category:OSWfecf99a9e5eb5ab384129063e12e07e7"]



class AreaRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'AreaRatio'
    """

    type: Optional[Any] = ["Category:OSW1e2d83c5660e50828bd14194ea5d5717"]



class Transmittance(DimensionlessRatio):
    """
    Transmittance is the fraction of incident light (electromagnetic radiation) at a specified wavelength that passes through a sample.
    """

    type: Optional[Any] = ["Category:OSW908b79aec1735ed1b08fb2947512ee6d"]



class AtmosphericHydroxylationRate(ReactionRateConstant):
    """
    A second order reaction rate constant that is a specific second order reaction rate constant that governs the kinetics of an atmospheric, gas-phase reaction between hydroxyl radicals and an organic chemical.
    """

    type: Optional[Any] = ["Category:OSW1213d5928a7956749688545e9526d6e3"]



class AbsorbedDose(SpecificEnergy):
    """
    "Absorbed Dose" (also known as Total Ionizing Dose, TID) is a measure of the energy deposited in a medium by ionizing radiation. It is equal to the energy deposited per unit mass of medium, and so has the unit $J/kg$, which is given the special name Gray ($Gy$).
    """

    type: Optional[Any] = ["Category:OSWb68921111fae5bcaa1d6128bc8be6615"]



class FissionMultiplicationFactor(Dimensionless):
    """
    The number of fission neutrons produced per absorption in the fuel.
    """

    type: Optional[Any] = ["Category:OSW394653a1d5f6545f8ea7babe10182f37"]



class GrossLiftOffWeight(Mass):
    """
    The sum of a rocket's inert mass and usable fluids and gases at sea level.
    """

    type: Optional[Any] = ["Category:OSW8061114fa3555012b53c39fca5cbc5a8"]



class ThermalAdmittance(CoefficientOfHeatTransfer):
    """
    The heat transfer coefficient is also known as thermal admittance in the sense that the material may be seen as admitting heat to flow.
    """

    type: Optional[Any] = ["Category:OSWb82f3ae5f1c25607aac38b12aba13dd7"]



class ReserveMass(Mass):
    """
    A quantity of mass held by Program/project management to mitigate the risk of over-predicted performance estimates, under predicted mass estimates, and future operational and mission specific requirements (program mass reserve, manager's mass reserve, launch window reserve, performance reserve, etc.).
    """

    type: Optional[Any] = ["Category:OSWaf4250ba95c2516c96eebc62f2ecfdc6"]



class TimeRatio(DimensionlessRatio):
    """
    This is an autogenerated partial class definition of 'TimeRatio'
    """

    type: Optional[Any] = ["Category:OSWda552423849a536c80fb7c6e0f85eca4"]



class Radius(Length):
    """
    In classical geometry, the "Radius" of a circle or sphere is any line segment from its center to its perimeter the radius of a circle or sphere is the length of any such segment.
    """

    type: Optional[Any] = ["Category:OSW57a45884de6052698141a5cbe4aaa4ac"]
