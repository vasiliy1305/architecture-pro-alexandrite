from flask import Flask

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

resource = Resource.create({"service.name": "service-b"})

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)


otlp_exporter = OTLPSpanExporter(
    endpoint="jaeger:4317",
    insecure=True,
)

span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)

app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route("/")
def index():
    return "Hello from service-b!\n"

@app.route("/health")
def health():
    return "OK\n"
