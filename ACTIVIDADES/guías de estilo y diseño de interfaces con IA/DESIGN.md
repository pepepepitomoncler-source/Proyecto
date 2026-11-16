# DESIGN.md — Guía de estilo del frontend de Check&Fit

> Check&Fit: aplicación web para entrenadores personales y clubes deportivos (frontend en React).
> Este fichero describe el sistema de diseño para pegarlo en prompts de IA y aplicarlo en código.

## Guía elegida
- **Nombre:** Material Design 3 (Material You), con tema propio generado a partir del verde de la marca.
- **Enlace oficial:** https://m3.material.io
- **Por qué la he elegido:**
  - Su color dinámico genera una paleta completa y accesible a partir de **un solo color semilla**. Así uso el verde del logo de Check&Fit (`#33D06D`) sin tener que inventarme el resto de colores.
  - Está pensada para apps multiplataforma: Check&Fit la usarán clientes desde el móvil en el gimnasio y entrenadores desde el ordenador.
  - Tiene implementación directa en React (MUI, `@material/web`) y sus tokens se publican como variables CSS (`--md-sys-color-*`).
  - Las formas redondeadas y los botones tipo píldora encajan con el tono cercano y deportivo de la marca. Fluent 2 o Carbon son más sobrios y están más orientadas a oficina.

## Colores (design tokens)
Generados con la librería oficial de Material (`@material/material-color-utilities`, la misma que usa **Material Theme Builder**). Esquema *Tonal Spot*, modo claro, semilla `#33D06D` (sacada del logo).

| Token | Valor | Uso |
|---|---|---|
| color-primary | `#336940` | Botones principales, enlaces, pestaña activa de la navegación |
| color-on-primary | `#FFFFFF` | Texto e iconos sobre el color primario |
| color-primary-container | `#B5F1BC` | Fondo de la tarjeta de resultado correcto, indicador de pestaña activa |
| color-on-primary-container | `#19512A` | Texto sobre primary-container |
| color-surface | `#F6FBF2` | Fondo de la página |
| color-surface-container | `#EBEFE7` | Cabecera (top app bar) y tarjetas neutras |
| color-on-surface | `#181D18` | Texto principal |
| color-on-surface-variant | `#414941` | Texto secundario, etiquetas, textos de ayuda |
| color-outline | `#717970` | Borde de los campos de texto |
| color-outline-variant | `#C1C9BE` | Separadores, borde de tarjetas |
| color-secondary | `#506352` | Anillo de foco de teclado |
| color-error | `#BA1A1A` | Texto/icono de error, borde de campo con error |
| color-on-error | `#FFFFFF` | Texto sobre color de error |
| color-error-container | `#FFDAD6` | Fondo del aviso de error |
| color-on-error-container | `#93000A` | Texto dentro del aviso de error |

**Colores de marca (solo para el logo, no para la interfaz):** verde `#33D06D`, negro `#000000`, blanco `#FFFFFF`.
⚠️ El verde de marca con texto blanco encima solo da **2,02:1** de contraste (no cumple). Por eso los botones usan `color-primary` (`#336940`, el tono 40 del mismo verde) y no el verde del logo.

## Tipografía
- **Familia:** Roboto (de serie en M3). En CSS: `font-family: 'Roboto', system-ui, sans-serif;`
- **Título de página:** Headline Small: 24 px / interlineado 32 px / peso 400
- **Título de tarjeta o sección:** Title Large: 22 px / 28 px / peso 400
- **Texto normal:** Body Large: 16 px / 24 px / peso 400 (Body Medium 14/20 para textos de ayuda)
- **Texto de botones y navegación:** Label Large: 14 px / 20 px / peso 500
- **Pesos utilizados:** 400 (regular) y 500 (medium)

## Espaciado y forma
- **Unidad base de espaciado:** 4 px (rejilla de 4 dp de M3). Lo habitual son múltiplos de 8.
- **Espaciados:** s = 8 px, m = 16 px, l = 24 px (xl = 32 px entre bloques)
- **Márgenes de página:** 16 px en móvil, 24 px en escritorio. Ancho máximo del contenido: 640 px.
- **Radio de los bordes (escala de forma M3):**
  - extra-small = 4 px → campos de texto (outlined)
  - medium = 12 px → tarjetas y avisos
  - full = 9999 px → botones (forma de píldora) e indicador de navegación

## Componentes
- **Cabecera (Top app bar):** fondo `surface-container`, alto 64 px, logo/nombre "Check&Fit" a la izquierda y navegación (Inicio, Hello) a la derecha. La pestaña activa lleva un indicador en píldora con `primary-container`.
- **Botón principal (Filled button):**
  - Forma de píldora (radio full), alto 40 px y padding horizontal de 24 px. Fondo `primary` y texto `on-primary`.
  - Texto en *sentence case* (no en mayúsculas), con estilo Label Large.
  - **Hover:** capa del color `on-primary` al 8 %. **Pulsado:** al 10 %.
  - **Deshabilitado:** fondo `on-surface` al 12 % y texto `on-surface` al 38 %.
  - **Foco:** anillo de 3 px en `secondary`, separado 2 px del botón.
- **Campo de texto (Outlined text field):**
  - Borde de 1 px en `outline` y radio de 4 px. Alto 56 px.
  - La etiqueta va dentro y **flota** sobre el borde cuando hay foco o texto. Puede llevar texto de ayuda debajo (Body Small, `on-surface-variant`).
  - **Con foco:** borde de 2 px en `primary` y etiqueta en `primary`.
- **Zona de resultado:** tarjeta *filled* de radio 12 px y padding de 16 px.
  - **Vacío:** fondo `surface-container` y texto de ayuda en `on-surface-variant`.
  - **Cargando:** indicador circular de progreso (indeterminado) en `primary` con el texto "Conectando…".
  - **Correcto:** fondo `primary-container` y texto `on-primary-container` en Title Large.
- **Mensaje de error:** tarjeta con fondo `error-container` y texto `on-error-container`, con un icono de error (círculo con "!") a la izquierda del texto. Va **en la propia zona de resultado**, debajo del botón. Lleva `role="alert"` para que lo anuncien los lectores de pantalla.

## Accesibilidad
- **Contraste mínimo del texto:** 4,5:1 (WCAG AA). Parejas comprobadas (fórmula WCAG 2.x, la misma que usa WebAIM Contrast Checker):
  | Texto / fondo | Contraste | ¿Cumple AA? |
  |---|---|---|
  | on-primary / primary | 6,49:1 | ✅ |
  | on-surface / surface | 16,29:1 | ✅ |
  | on-surface-variant / surface | 8,87:1 | ✅ |
  | primary / surface (enlaces) | 6,18:1 | ✅ |
  | on-primary-container / primary-container | 7,23:1 | ✅ |
  | on-error-container / error-container | 7,24:1 | ✅ |
  | error / surface | 6,15:1 | ✅ |
  | outline / surface (borde de campo, mínimo 3:1) | 4,28:1 | ✅ |
  | blanco / verde de marca `#33D06D` | 2,02:1 | ❌ → no se usa en la interfaz |
- **Foco visible:** anillo de 3 px en `secondary` (`#506352`), separado 2 px, solo con teclado (`:focus-visible`). Nunca se usa `outline: none` sin poner otra alternativa.
- **Todos los campos tienen etiqueta visible**, asociada con `<label for>`. El campo "Nombre" indica "(opcional)" en la propia etiqueta.
- La zona de resultado lleva `aria-live="polite"` y el error, `role="alert"`.
- Zona táctil mínima de 48 × 48 px en botones y enlaces de navegación.
- El estado no se comunica solo con color: el error lleva icono y texto, y la carga lleva texto además del spinner.

## Tono de los textos
- **Cercano**, de **tú** (como un entrenador): "Escribe tu nombre", "¡Vamos!".
- Mensajes **cortos**, de una frase. Botones con verbos de acción ("Saludar", "Ir al saludo").
- Los errores dicen qué ha pasado y qué hacer, sin culpar al usuario: "No se ha podido contactar con el backend. Inténtalo de nuevo en unos segundos."
