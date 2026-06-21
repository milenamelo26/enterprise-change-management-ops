---

## 4. Boilerplate de Código Limpio

```python
import os
from typing import List
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# =====================================================================
# 1. ESQUEMAS DE DATOS RIGUROSOS (Target para People Analytics)
# =====================================================================
class PMOBottleneckReport(BaseModel):
    bottleneck_detected: bool = Field(
        description="True if structural task concentration or capacity risks are found."
    )
    overloaded_generic_roles: List[str] = Field(
        description="List of anonymized functions or departments exhibiting high friction (e.g., 'Core Tech', 'Facilities')."
    )
    burnout_risk_index: str = Field(
        description="Qualitative risk score ('High', 'Medium', 'Low') evaluating stress indicators based on deadlines."
    )
    strategic_rebalancing_advice: str = Field(
        description="Data-driven organizational recommendation to optimize human capital allocation."
    )

# =====================================================================
# 2. MOTOR DE AGENTE AUTÓNOMO DE EVALUACIÓN
# =====================================================================
class ChangeManagementAIEngine:
    def __init__(self):
        # Inicialización del cliente moderno oficial de Google GenAI
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("[CRITICAL ERROR]: The GEMINI_API_KEY environment variable must be set.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-1.5-flash" # Optimizado para alta velocidad y costo-eficiencia

    def run_workload_audit(self, anonymized_json_payload: str) -> PMOBottleneckReport:
        """
        Ingests real-time raw project data and returns a structured analytical report.
        """
        system_instruction = (
            "You are an Elite Enterprise PMO Intelligence Architect and Organizational Psychologist. "
            "Your mandate is to analyze unstructured operational metadata to detect capacity bottlenecks "
            "and human resources friction. You must strictly satisfy the requested Pydantic JSON schema."
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=f"Analyze the following operational dataset:\n\n{anonymized_json_payload}",
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.1,  # Temperatura baja para asegurar consistencia determinista
                    response_mime_type="application/json",
                    response_schema=PMOBottleneckReport,
                ),
            )
            # El SDK realiza el parsing automático al tipo Pydantic solicitado
            return response.parsed
        except Exception as error:
            print(f"[PIPELINE RUNTIME ERROR]: Analysis execution halted: {str(error)}")
            raise

# =====================================================================
# 3. INTERFAZ DE PRUEBA: GENERACIÓN DE DATOS SINTÉTIOS ANÓNIMOS
# =====================================================================
if __name__ == "__main__":
    # Generación manual de datos sintéticos puros (Garantía absoluta de privacidad empresarial)
    synthetic_pmo_backlog = """
    [
      {"task_id": "T-001", "title": "Decommission server racks", "status": "pending", "assigned_role": "Infrastructure Tech", "priority": "critical"},
      {"task_id": "T-002", "title": "Re-wire secondary data center", "status": "pending", "assigned_role": "Infrastructure Tech", "priority": "high"},
      {"task_id": "T-003", "title": "Audit power backup supply", "status": "in_progress", "assigned_role": "Infrastructure Tech", "priority": "critical"}
    ]
    """
    
    print("Initializing Zero-Trust PMO Load Balancing Pipeline...")
    engine = ChangeManagementAIEngine()
    
    try:
        # Ejecución simulada limpia de nivel de producción
        structured_analytics = engine.run_workload_audit(synthetic_pmo_backlog)
        print("\n--- [CONSOLIDATED PEOPLE ANALYTICS INSIGHTS] ---")
        print(structured_analytics.model_dump_json(indent=2))
    except Exception:
        print("\n[EXECUTION FAILED]: Verify engine authentication configuration.")
