<?php

namespace App\Http\Controllers;

use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class HelloController extends Controller
{
    /**
     * GET /api/hello
     * GET /api/hello?name=Ana
     */
    public function index(Request $request): JsonResponse
    {
        // Reto extra 1: "name" es opcional y como mucho de 50 caracteres.
        // Se usa Validator::make para devolver SIEMPRE JSON con 422
        // (con $request->validate() una petición sin "Accept: application/json"
        // recibiría una redirección en lugar del error en JSON).
        $validator = Validator::make($request->query(), [
            'name' => ['nullable', 'string', 'max:50'],
        ]);

        if ($validator->fails()) {
            return response()->json([
                'message' => 'El nombre no puede tener más de 50 caracteres.',
                'errors' => $validator->errors(),
            ], 422);
        }

        // Leemos el parámetro "name" de la query string (o cadena vacía si no viene)
        $name = trim((string) $request->query('name', ''));

        $message = $name === ''
            ? 'Hello World'
            : "Hello World {$name}";

        return response()->json([
            'message' => $message,
        ]);
    }
}
