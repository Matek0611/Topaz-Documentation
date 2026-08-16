---
tags:
    - Standard Library
    - Core Library
    - Math
---

# Functions

## Basic Math & Range Utilities

| Function      | Parameters        | Return Type   |           Formula           | Description                                                                  |
|---------------|-------------------|---------------|:---------------------------:|------------------------------------------------------------------------------|
| `Abs`         | `x: LongInteger`  | `LongInteger` |       $\vert x\vert$        | Calculates the absolute value of an integer or scalar.                       |
| `FAbs`        | `x: Double`       | `Double`      |       $\vert x\vert$        | Calculates the floating-point absolute value.                                |
| `Sign`        | `x: Double`       | `Integer`     |      $\textrm{sgn}(x)$      | Returns `-1` if $x < 0$, 0 if $x = 0$, and `1` if $x > 0$.                   |
| `Min`         | `@VarArgs`        | `Auto`        |    $\min(x_1, x_2, ...)$    | Returns the minimum value among the arguments.                               |
| `Max`         | `@VarArgs`        | `Auto`        |    $\max(x_1, x_2, ...)$    | Returns the maximum value among the arguments.                               |
| `EnsureRange` | `(x, a, b): Auto` | `Auto`        |    $\min(\max(x, a), b)$    | Clamps $x$ to the closed interval $\langle a, b\rangle$.                     |
| `InRange`     | `(x, a, b): Auto` | `Boolean`     | $x \in \langle a, b\rangle$ | Returns `True` if $x$ lies within the inclusive range $\langle a, b\rangle$. |

## Rounding & Truncation

| Function   | Parameters  | Return Type   |          Formula          | Description                                                |
|------------|-------------|---------------|:-------------------------:|------------------------------------------------------------|
| `Ceiling`  | `x: Double` | `LongInteger` |     $\lceil x \rceil$     | Smallest integer greater than or equal to $x$.             |
| `Floor`    | `x: Double` | `LongInteger` |    $\lfloor x \rfloor$    | Largest integer less than or equal to $x$.                 |
| `Truncate` | `x: Double` | `LongInteger` | $\operatorname{trunc}(x)$ | Removes the fractional part of $x$, rounding towards zero. |

## Floating-Point Inspection Predicates

Boolean functions to inspect IEEE 754 floating-point values.

| Function     | Parameters  | Return Type | Description                                                                  |
|--------------|-------------|-------------|------------------------------------------------------------------------------|
| `IsNaN`      | `x: Double` | `Boolean`   | Returns `True` if $x$ represents Not-a-Number.                               |
| `IsInfinite` | `x: Double` | `Boolean`   | Returns `True` if $x$ represents $\pm\infty$.                                |
| `IsFinite`   | `x: Double` | `Boolean`   | Returns `True` if $x$ is a valid finite number (neither `NaN` nor infinite). |

## Exponential & Logarithmic Functions

| Function        | Parameters       | Return Type |    Formula    | Description                                  |
|-----------------|------------------|-------------|:-------------:|----------------------------------------------|
| `Exp`           | `x: Double`      | `Double`    |     $e^x$     | Computes the natural exponential of $x$.     |
| `Ln`            | `x: Double`      | `Double`    |   $\ln(x)$    | Natural logarithm (base $e$).                |
| `Log` / `Log10` | `x: Double`      | `Double`    |   $\log(x)$   | Common logarithm (base $10$).                |
| `Log2`          | `x: Double`      | `Double`    | $\log_{2}(x)$ | Binary logarithm (base $2$).                 |
| `LogN`          | `(b, x): Double` | `Double`    | $\log_{b}(x)$ | Logarithm of $x$ with an arbitrary base $b$. |

## Combinatorics & Number Theory

| Function    | Parameters                | Return Type   |               Formula                | Description                                                                                          |
|-------------|---------------------------|---------------|:------------------------------------:|------------------------------------------------------------------------------------------------------|
| `Factorial` | `x: TinyNatural`          | `LongNatural` |                 $n!$                 | Calculates $n$ factorial ($n! = 1 \cdot 2 \cdot\ ...\ \cdot n$). Note: $n \in \langle 0, 20\rangle$. |
| `NCK`       | `(n, k): Natural`         | `Double`      | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Binomial coefficient ("$n$ choose $k$").                                                             |
| `GCD`       | `x: array of LongNatural` | `LongNatural` |  $\operatorname{gcd}(a, b, \dots)$   | Greatest Common Divisor of two or more integers.                                                     |
| `LCM`       | `x: array of LongNatural` | `LongNatural` |  $\operatorname{lcm}(a, b, \dots)$   | Least Common Multiple of two or more integers.                                                       |
| `Hypot`     | `(x, y): Double`          | `Double`      |          $\sqrt{x^2 + y^2}$          | Computes the Euclidean distance / hypotenuse without overflow.                                       |

## Special Functions

| Function  | Parameters  | Return Type |                                Formula                                 | Description                                                            |
|-----------|-------------|-------------|:----------------------------------------------------------------------:|------------------------------------------------------------------------|
| `Gamma`   | `x: Double` | `Double`    |             $\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$              | Euler's Gamma function (generalization of factorial).                  |
| `LnGamma` | `x: Double` | `Double`    |                             $\ln\Gamma(x)$                             | Natural logarithm of the Gamma function.                               |
| `Erf`     | `x: Double` | `Double`    |  $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt$   | Gauss Error Function.                                                  |
| `Erfc`    | `x: Double` | `Double`    |          $\operatorname{erfc}(x) = 1 - \operatorname{erf}(x)$          | Complementary Error Function.                                          |
| `Sinc`    | `x: Double` | `Double`    |                          $\frac{\sin(x)}{x}$                           | Cardinal sine function. Note: $\operatorname{sinc}(0) = 1$.            |
| `Sinhc`   | `x: Double` | `Double`    |                          $\frac{\sinh(x)}{x}$                          | Hyperbolic cardinal sine function Note: $\operatorname{sinhc}(0) = 1$. |
| `ArcSinc` | `x: Double` | `Double`    |        $\operatorname{sinc}^{-1}(y)$ or $\frac{\arcsin(x)}{x}$         | Inverse or cardinal arc-sine function.                                 |
| `ArSinhc` | `x: Double` | `Double`    | $\operatorname{sinhc}^{-1}(y)$ or $\frac{\operatorname{arsinh}(x)}{x}$ | Inverse or cardinal hyperbolic arc-sine function.                      |

## Angle Conversion & Normalization

| Function           | Parameters  | Return Type |          Formula          | Description                                                      |
|--------------------|-------------|-------------|:-------------------------:|------------------------------------------------------------------|
| `DegToRad`         | `x: Double` | `Double`    | $x \cdot \frac{\pi}{180}$ | Converts degrees to radians.                                     |
| `RadToDeg`         | `x: Double` | `Double`    | $x \cdot \frac{180}{\pi}$ | Converts radians to degrees.                                     |
| `GradToRad`        | `x: Double` | `Double`    | $x \cdot \frac{\pi}{200}$ | Converts gradians to radians.                                    |
| `RadToGrad`        | `x: Double` | `Double`    | $x \cdot \frac{200}{\pi}$ | Converts radians to gradians.                                    |
| `DegToGrad`        | `x: Double` | `Double`    | $x \cdot \frac{200}{180}$ | Converts degrees to gradians.                                    |
| `GradToDeg`        | `x: Double` | `Double`    | $x \cdot \frac{200}{180}$ | Converts gradians to degrees.                                    |
| `NormalizeDegrees` | `x: Double` | `Double`    |      $x \pmod{360}$       | Normalizes an angle in degrees into the range $\langle 0, 360)$. |

## Trigonometric Functions

### Standard & Secondary Trigonometric Functions

All functions expect input angles in **radians**.

| Function | Parameters  | Return Type |            Formula            | Description         |
|----------|-------------|-------------|:-----------------------------:|---------------------|
| `Sin`    | `x: Double` | `Double`    |           $\sin(x)$           | Sine function.      |
| `Cos`    | `x: Double` | `Double`    |           $\cos(x)$           | Cosine function.    |
| `Tan`    | `x: Double` | `Double`    |           $\tan(x)$           | Tangent function.   |
| `Cot`    | `x: Double` | `Double`    | $\cot(x) = \frac{1}{\tan(x)}$ | Cotangent function. |
| `Sec`    | `x: Double` | `Double`    | $\sec(x) = \frac{1}{\cos(x)}$ | Secant function.    |
| `Csc`    | `x: Double` | `Double`    | $\csc(x) = \frac{1}{\sin(x)}$ | Cosecant function.  |

### Auxiliary & Historical Functions

Specialized trigonometric functions used in spherical navigation and classical geometry.

| Function | Parameters  | Return Type |                         Formula                         | Description              |
|----------|-------------|-------------|:-------------------------------------------------------:|--------------------------|
| `Crd`    | `x: Double` | `Double`    | $\operatorname{crd}(x) = 2\sin\left(\frac{x}{2}\right)$ | Chord function.          |
| `Vers`   | `x: Double` | `Double`    |         $\operatorname{vers}(x) = 1 - \cos(x)$          | Versine (versed cosine). |
| `Hav`    | `x: Double` | `Double`    |     $\operatorname{hav}(x) = \frac{1 - \cos(x)}{2}$     | Haversine.               |
| `Covers` | `x: Double` | `Double`    |        $\operatorname{covers}(x) = 1 - \sin(x)$         | Coversine (versed sine). |
| `Exsec`  | `x: Double` | `Double`    |         $\operatorname{exsec}(x) = \sec(x) - 1$         | Exsecant.                |

## Inverse Trigonometric Functions

Functions return angles in radians.

| Function    | Parameters  | Return Type |                           Formula                            | Description                  |
|-------------|-------------|-------------|:------------------------------------------------------------:|------------------------------|
| `ArcSin`    | `y: Double` | `Double`    |                         $\arcsin(y)$                         | Arc-sine ($\sin^{-1}$).      |
| `ArcCos`    | `y: Double` | `Double`    |                         $\arccos(y)$                         | Arc-cosine ($\cos^{-1}$).    |
| `ArcTan`    | `y: Double` | `Double`    |                         $\arctan(y)$                         | Arc-tangent ($\tan^{-1}$).   |
| `ArcCot`    | `y: Double` | `Double`    |                  $\operatorname{arccot}(y)$                  | Arc-cotangent ($\cot^{-1}$). |
| `ArcSec`    | `y: Double` | `Double`    | $\operatorname{arcsec}(y) = \arccos\left(\frac{1}{y}\right)$ | Arc-secant ($\sec^{-1}$).    |
| `ArcCsc`    | `y: Double` | `Double`    | $\operatorname{arccsc}(y) = \arcsin\left(\frac{1}{y}\right)$ | Arc-cosecant ($\csc^{-1}$).  |
| `ArcCrd`    | `y: Double` | `Double`    |              $2\arcsin\left(\frac{y}{2}\right)$              | Inverse chord function.      |
| `ArcVers`   | `y: Double` | `Double`    |                       $\arccos(1 - y)$                       | Inverse versine function.    |
| `ArcHav`    | `y: Double` | `Double`    |                     $2\arcsin(\sqrt{y})$                     | Inverse haversine function.  |
| `ArcCovers` | `y: Double` | `Double`    |                       $\arcsin(1 - y)$                       | Inverse coversine function.  |
| `ArcExsec`  | `y: Double` | `Double`    |            $\arccos\left(\frac{1}{1 + y}\right)$             | Inverse exsecant function.   |

## Hyperbolic Functions

| Function  | Parameters  | Return Type |                    Formula                    | Description                                        |
|-----------|-------------|-------------|:---------------------------------------------:|----------------------------------------------------|
| `SinH`    | `x: Double` | `Double`    |      $\sinh(x) = \frac{e^x - e^{-x}}{2}$      | Hyperbolic sine.                                   |
| `CosH`    | `x: Double` | `Double`    |      $\cosh(x) = \frac{e^x + e^{-x}}{2}$      | Hyperbolic cosine.                                 |
| `TanH`    | `x: Double` | `Double`    |    $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$     | Hyperbolic tangent.                                |
| `CotH`    | `x: Double` | `Double`    |    $\coth(x) = \frac{\cosh(x)}{\sinh(x)}$     | Hyperbolic cotangent.                              |
| `SecH`    | `x: Double` | `Double`    | $\operatorname{sech}(x) = \frac{1}{\cosh(x)}$ | Hyperbolic secant.                                 |
| `CscH`    | `x: Double` | `Double`    | $\operatorname{csch}(x) = \frac{1}{\sinh(x)}$ | Hyperbolic cosecant.                               |
| `HCrd`    | `u: Double` | `Double`    |       $2\sinh\left(\frac{u}{2}\right)$        | Hyperbolic chord.                                  |
| `HVers`   | `u: Double` | `Double`    |                $\cosh(u) - 1$                 | Hyperbolic versine ($\operatorname{vercosh}$).     |
| `HHav`    | `u: Double` | `Double`    |           $\frac{\cosh(u) - 1}{2}$            | Hyperbolic haversine ($\operatorname{havercosh}$). |
| `HCovers` | `u: Double` | `Double`    |                $1 - \sinh(u)$                 | Hyperbolic coversine ($\operatorname{coversinh}$). |
| `ExsecH`  | `u: Double` | `Double`    |         $\operatorname{sech}(u) - 1$          | Hyperbolic exsecant.                               |

## Inverse Hyperbolic Functions

| Function    | Parameters  | Return Type |                                  Formula                                   | Description                   |
|-------------|-------------|-------------|:--------------------------------------------------------------------------:|-------------------------------|
| `ArSinH`    | `y: Double` | `Double`    |      $\operatorname{arsinh}(y) = \ln\left(y + \sqrt{y^2 + 1}\right)$       | Inverse hyperbolic sine.      |
| `ArCosH`    | `y: Double` | `Double`    |      $\operatorname{arcosh}(y) = \ln\left(y + \sqrt{y^2 - 1}\right)$       | Inverse hyperbolic cosine.    |
| `ArTanH`    | `y: Double` | `Double`    |  $\operatorname{artanh}(y) = \frac{1}{2}\ln\left(\frac{1+y}{1-y}\right)$   | Inverse hyperbolic tangent.   |
| `ArCotH`    | `y: Double` | `Double`    |  $\operatorname{arcoth}(y) = \frac{1}{2}\ln\left(\frac{y+1}{y-1}\right)$   | Inverse hyperbolic cotangent. |
| `ArSecH`    | `y: Double` | `Double`    | $\operatorname{arsech}(y) = \operatorname{arcosh}\left(\frac{1}{y}\right)$ | Inverse hyperbolic secant.    |
| `ArCscH`    | `y: Double` | `Double`    | $\operatorname{arcsch}(y) = \operatorname{arsinh}\left(\frac{1}{y}\right)$ | Inverse hyperbolic cosecant.  |
| `ArHCrd`    | `y: Double` | `Double`    |              $2\operatorname{arsinh}\left(\frac{y}{2}\right)$              | Inverse hyperbolic chord.     |
| `ArHVers`   | `y: Double` | `Double`    |                       $\operatorname{arcosh}(1 + y)$                       | Inverse hyperbolic versine.   |
| `ArHHav`    | `y: Double` | `Double`    |                     $2\operatorname{arsinh}(\sqrt{y})$                     | Inverse hyperbolic haversine. |
| `ArHCovers` | `y: Double` | `Double`    |                       $\operatorname{arsinh}(1 - y)$                       | Inverse hyperbolic coversine. |
| `ArExsecH`  | `y: Double` | `Double`    |            $\operatorname{arcosh}\left(\frac{1}{1 + y}\right)$             | Inverse hyperbolic exsecant.  |

