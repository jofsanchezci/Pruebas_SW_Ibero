
# Fundamentos de las Pruebas del Producto de Software

## 1. Definición de Pruebas de Software
Las pruebas de software son un proceso sistemático para identificar defectos en un producto de software. Tienen como objetivo evaluar si el software cumple con las expectativas definidas en los requerimientos y si es adecuado para su propósito.

---

## 2. Objetivos de las Pruebas
1. **Verificar la funcionalidad:** Confirmar que el software cumple con los requisitos especificados.
2. **Detectar defectos:** Identificar errores, fallos o anomalías antes del despliegue.
3. **Asegurar calidad:** Garantizar la confiabilidad, eficiencia, seguridad y usabilidad.
4. **Mejorar la confianza:** Incrementar la confianza en el software para todas las partes interesadas.

---

## 3. Principios Fundamentales de las Pruebas
1. **Ausencia de errores no significa calidad:** El hecho de que las pruebas no detecten defectos no garantiza que el software sea perfecto.
2. **Pruebas exhaustivas son imposibles:** No es viable probar todos los casos posibles; se priorizan las pruebas más críticas.
3. **Pruebas tempranas:** Es más eficiente y económico detectar errores en las primeras etapas del desarrollo.
4. **Agrupación de defectos:** Los defectos tienden a concentrarse en ciertas áreas del software.
5. **Paradoja del pesticida:** Repetir las mismas pruebas constantemente puede no encontrar nuevos defectos; es necesario actualizarlas.
6. **Dependencia del contexto:** Las pruebas deben adaptarse al tipo de sistema (web, móvil, embebido, etc.).
7. **Error humano:** Los errores en las pruebas también pueden ser producto de fallos en los casos de prueba o en su ejecución.

---

## 4. Tipos de Pruebas
1. **Funcionales:** Evalúan las funciones específicas del software en base a los requisitos.
   - Ejemplo: Pruebas de caja negra, pruebas de integración.
2. **No funcionales:** Analizan aspectos como rendimiento, escalabilidad y seguridad.
   - Ejemplo: Pruebas de carga, estrés y penetración.
3. **Estructurales:** Exploran la estructura interna del software.
   - Ejemplo: Pruebas de caja blanca.
4. **De cambio:** Verifican modificaciones en el software.
   - Ejemplo: Pruebas de regresión y de humo.

---

## 5. Proceso de Pruebas
1. **Análisis de requerimientos:** Identificar qué aspectos del software deben probarse.
2. **Diseño de casos de prueba:** Definir las entradas, acciones y resultados esperados.
3. **Configuración del entorno:** Preparar el ambiente adecuado para ejecutar las pruebas.
4. **Ejecución:** Realizar las pruebas y registrar los resultados.
5. **Evaluación:** Comparar los resultados reales con los esperados.
6. **Reporte de defectos:** Documentar los errores encontrados.
7. **Cierre:** Confirmar que los defectos críticos han sido resueltos y que el producto cumple los estándares de calidad.

---

## 6. Herramientas Comunes de Pruebas
1. **Automatización:** Selenium, JUnit, TestNG, Appium.
2. **Gestión de pruebas:** TestRail, Zephyr.
3. **Pruebas de carga y rendimiento:** JMeter, LoadRunner.
4. **Pruebas de seguridad:** OWASP ZAP, Burp Suite.

---

## 7. Roles en el Proceso de Pruebas
1. **Tester o QA Engineer:** Realiza y diseña las pruebas.
2. **Desarrollador:** Ejecuta pruebas unitarias y soluciona defectos.
3. **Administrador de pruebas:** Coordina actividades y asegura el cumplimiento del plan.
4. **Product Owner:** Verifica la conformidad con los objetivos del producto.

---

## 8. Métricas en las Pruebas de Software
- Porcentaje de casos de prueba ejecutados.
- Tasa de defectos encontrados por módulo.
- Tasa de resolución de defectos.
- Cobertura de código probada.

---

Las pruebas de software son esenciales para garantizar un producto confiable y satisfactorio para los usuarios finales, reduciendo costos a largo plazo al prevenir problemas en etapas posteriores.

# Pruebas del Script `rectangle.py`

Este archivo describe cómo funcionan las pruebas para el script `rectangle.py`, que incluye una función para calcular el área de un rectángulo. 

## 1. Estructura del Proyecto

El proyecto contiene los siguientes archivos principales:

- `rectangle.py`: Contiene la lógica de la función `calculate_area` que se encarga de calcular el área de un rectángulo.
- `test_rectangle.py`: Archivo que contiene las pruebas unitarias para validar la funcionalidad de la función `calculate_area`.

---

## 2. Descripción de la Función a Probar

La función `calculate_area(length, width)` está diseñada para calcular el área de un rectángulo. Su comportamiento es el siguiente:

- **Parámetros:**
  - `length`: Longitud del rectángulo (debe ser un número no negativo).
  - `width`: Ancho del rectángulo (debe ser un número no negativo).
  
- **Salida:**
  - Devuelve el área del rectángulo como un número.
  
- **Excepciones:**
  - Lanza un `ValueError` si se pasan valores negativos para la longitud o el ancho.

---

## 3. Cómo Funcionan las Pruebas

El archivo `test_rectangle.py` utiliza el módulo `unittest` para realizar pruebas automáticas de la función `calculate_area`. 

### 3.1. Pruebas Incluidas

1. **Pruebas de Cálculo de Área:**
   - Verifica que la función devuelve los valores esperados para entradas válidas.
   - Ejemplo: `calculate_area(5, 3)` debería devolver `15`.

2. **Pruebas con Valores Cero:**
   - Verifica que la función maneja correctamente los casos donde la longitud o el ancho son cero.
   - Ejemplo: `calculate_area(0, 5)` debería devolver `0`.

3. **Pruebas con Valores Negativos:**
   - Valida que la función lanza un `ValueError` cuando se pasan valores negativos como parámetros.
   - Ejemplo: `calculate_area(-1, 5)` debería lanzar una excepción.

---

## 4. Cómo Ejecutar las Pruebas

Sigue estos pasos para ejecutar las pruebas:

1. Asegúrate de que los archivos `rectangle.py` y `test_rectangle.py` estén en el mismo directorio.
2. Abre una terminal y navega al directorio donde están los archivos.
3. Ejecuta las pruebas con el siguiente comando:

   ```bash
   python -m unittest test_rectangle.py
   ```

---

## 5. Resultado Esperado

Si todas las pruebas pasan correctamente, deberías ver un mensaje como este:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

Si alguna prueba falla, el mensaje mostrará qué prueba falló, junto con información útil para depurar el problema.

---
