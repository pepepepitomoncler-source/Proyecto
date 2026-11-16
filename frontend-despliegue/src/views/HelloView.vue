<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getHello } from '@/services/helloService'
import HelloResult from '@/components/HelloResult.vue'

const route = useRoute()
const router = useRouter()

// Estado de la vista
const name = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

// Acción: se ejecuta al enviar el formulario
async function saludar() {
  loading.value = true
  error.value = ''
  message.value = ''

  // Reto extra 1: el nombre queda en la URL (/hello?name=Ana)
  const cleanName = name.value.trim()
  router.replace({ query: cleanName ? { name: cleanName } : {} })

  try {
    message.value = await getHello(name.value)
  } catch (e) {
    error.value = 'Comprueba que el backend está arrancado e inténtalo de nuevo en unos segundos.'
    console.error(e)
  } finally {
    loading.value = false
  }
}

// Reto extra 1: si se entra con /hello?name=Ana, rellena el campo y saluda solo
onMounted(() => {
  const queryName = route.query.name
  if (typeof queryName === 'string' && queryName.trim() !== '') {
    name.value = queryName
    saludar()
  }
})
</script>

<template>
  <section class="hello">
    <h1>Hello World</h1>
    <p class="hello__intro">Escribe tu nombre (o déjalo vacío) y pulsa «Saludar».</p>

    <form class="hello__form" @submit.prevent="saludar">
      <!-- Outlined text field de M3 con etiqueta flotante -->
      <div class="field">
        <input
          id="name"
          v-model="name"
          type="text"
          placeholder=" "
          autocomplete="given-name"
          aria-describedby="name-help"
        />
        <label for="name">Nombre (opcional)</label>
        <span id="name-help" class="field__support">Si lo dejas vacío verás «Hello World».</span>
      </div>

      <button type="submit" class="btn-filled" :disabled="loading">
        {{ loading ? 'Cargando…' : 'Saludar' }}
      </button>
    </form>

    <HelloResult :message="message" :error="error" :loading="loading" />
  </section>
</template>

<style scoped>
.hello__intro {
  color: var(--color-on-surface-variant);
}

.hello__form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: var(--space-m);
}

/* ===== Outlined text field ===== */
.field {
  position: relative;
  width: 100%;
  max-width: 400px;
}

.field input {
  width: 100%;
  height: 56px;
  padding: var(--space-m);
  border: 1px solid var(--color-outline);
  border-radius: var(--radius-xs);
  background: transparent;
  color: var(--color-on-surface);
  font: inherit;
}

.field input:hover {
  border-color: var(--color-on-surface);
}

/* Con foco: borde de 2 px en primary (se compensa el padding para que no salte) */
.field input:focus {
  outline: none;
  border: 2px solid var(--color-primary);
  padding: 15px;
}

.field label {
  position: absolute;
  top: 16px;
  left: 12px;
  padding: 0 var(--space-xs);
  background: var(--color-surface);
  color: var(--color-on-surface-variant);
  pointer-events: none;
  transition: all 0.15s;
}

/* Etiqueta flotante: sube al borde con foco o cuando hay texto */
.field input:focus + label,
.field input:not(:placeholder-shown) + label {
  top: -8px;
  font-size: var(--font-size-small);
  line-height: 16px;
}

.field input:focus + label {
  color: var(--color-primary);
}

.field__support {
  display: block;
  padding: var(--space-xs) var(--space-m) 0;
  font-size: var(--font-size-small);
  color: var(--color-on-surface-variant);
}
</style>
