import { WebTracerProvider } from '@opentelemetry/sdk-trace-web'
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base'
import { W3CTraceContextPropagator } from '@opentelemetry/core'
import { registerInstrumentations } from '@opentelemetry/instrumentation'
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions'
import { Resource } from '@opentelemetry/resources'
import { ZoneContextManager } from '@opentelemetry/context-zone'
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch'
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'

export const initInstrumentation = () => {
  const exporter = new OTLPTraceExporter({
    url: `${process.env.REACT_APP_OTEL_COLLECTOR_ENDPOINT}/v1/traces`,
    // url: `${process.env.OTEL_COLLECTOR_DAEMON_ADDRESS}/trace`,
  })
console.log(`Connecting to ${process.env.REACT_APP_OTEL_COLLECTOR_ENDPOINT}/v1/traces collector`)

  const resource = new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'cruddur-frontend',
    application: 'crddur',
  })

  const provider = new WebTracerProvider({ resource })
  provider.addSpanProcessor(new BatchSpanProcessor(exporter))

  // Initialize the provider
  provider.register({
    propagator: new W3CTraceContextPropagator(),
    contextManager: new ZoneContextManager(),
  })

  // Registering instrumentations / plugins
  registerInstrumentations({
    instrumentations: [
      new FetchInstrumentation({
        propagateTraceHeaderCorsUrls: [/.+/g], // this is too broad for production
        clearTimingResources: true,
      }),
    ],
  })
}

export default initInstrumentation