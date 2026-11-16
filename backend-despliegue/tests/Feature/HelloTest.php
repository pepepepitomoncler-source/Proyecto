<?php

namespace Tests\Feature;

use Tests\TestCase;

class HelloTest extends TestCase
{
    public function test_saludo_sin_nombre(): void
    {
        $this->getJson('/api/hello')
            ->assertOk()
            ->assertExactJson(['message' => 'Hello World']);
    }

    public function test_saludo_con_nombre(): void
    {
        $this->getJson('/api/hello?name=Ana')
            ->assertOk()
            ->assertExactJson(['message' => 'Hello World Ana']);
    }

    public function test_saludo_con_nombre_vacio(): void
    {
        $this->getJson('/api/hello?name=')
            ->assertOk()
            ->assertExactJson(['message' => 'Hello World']);
    }

    public function test_saludo_con_tildes_y_espacios(): void
    {
        $this->getJson('/api/hello?name='.urlencode('  Ana García  '))
            ->assertOk()
            ->assertExactJson(['message' => 'Hello World Ana García']);
    }

    public function test_nombre_demasiado_largo_devuelve_422(): void
    {
        $this->getJson('/api/hello?name='.str_repeat('a', 51))
            ->assertStatus(422)
            ->assertJsonValidationErrors('name');
    }

    public function test_cors_permite_el_frontend(): void
    {
        $this->getJson('/api/hello', ['Origin' => 'http://localhost:5173'])
            ->assertHeader('Access-Control-Allow-Origin', 'http://localhost:5173');
    }

    public function test_cors_no_permite_otros_origenes(): void
    {
        $this->getJson('/api/hello', ['Origin' => 'http://web-maliciosa.com'])
            ->assertOk()
            ->assertHeaderMissing('Access-Control-Allow-Origin');
    }
}
