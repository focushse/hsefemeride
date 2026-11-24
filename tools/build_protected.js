/**
 * Build Script: Protege y ofusca el código fuente de Archivo HSE para producción
 */
const fs = require('fs');
const path = require('path');
const JavaScriptObfuscator = require('javascript-obfuscator');

const sourceFile = path.join(__dirname, '..', 'src_dev', 'index.html');
const distFile = path.join(__dirname, '..', 'index.html');

console.log('🛡️  Iniciando proceso de ofuscación y protección de Archivo HSE...');

if (!fs.existsSync(sourceFile)) {
  console.error('❌ Error: No se encontró el archivo fuente en', sourceFile);
  process.exit(1);
}

let html = fs.readFileSync(sourceFile, 'utf8');

// 1. Extraer el bloque <script> principal
const scriptStartTag = '<script>';
const scriptEndTag = '</script>';

const startIdx = html.indexOf(scriptStartTag);
const endIdx = html.lastIndexOf(scriptEndTag);

if (startIdx === -1 || endIdx === -1) {
  console.error('❌ Error: No se pudo identificar el bloque <script> principal.');
  process.exit(1);
}

const beforeScript = html.substring(0, startIdx + scriptStartTag.length);
const scriptContent = html.substring(startIdx + scriptStartTag.length, endIdx);
const afterScript = html.substring(endIdx);

console.log(`📄 Código JavaScript original extraído: ${(scriptContent.length / 1024).toFixed(1)} KB`);

// 2. Inyectar protección anti-copia y bloqueo de DevTools al inicio del script
const antiCopyGuard = `
(function() {
  // Bloqueo de menú contextual (clic derecho)
  document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
  }, { capture: true });

  // Bloqueo de teclas de inspección (F12, Ctrl+U, Ctrl+Shift+I, etc.)
  document.addEventListener('keydown', function(e) {
    if (
      e.key === 'F12' ||
      (e.ctrlKey && (e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S')) ||
      (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c'))
    ) {
      e.preventDefault();
      return false;
    }
  }, { capture: true });
})();
`;

const codeToObfuscate = antiCopyGuard + '\n' + scriptContent;

console.log('⚙️  Ofuscando lógica, base de datos y generador PDF con JavaScript-Obfuscator...');

const obfuscationResult = JavaScriptObfuscator.obfuscate(codeToObfuscate, {
  compact: true,
  controlFlowFlattening: false,
  deadCodeInjection: false,
  debugProtection: false, // Desactivado para no ralentizar navegadores móviles
  disableConsoleOutput: true,
  identifierNamesGenerator: 'hexadecimal',
  numbersToExpressions: true,
  renameGlobals: false,
  selfDefending: false,
  simplify: true,
  splitStrings: true,
  splitStringsChunkLength: 10,
  stringArray: true,
  stringArrayCallsTransform: true,
  stringArrayEncoding: ['base64'],
  stringArrayThreshold: 0.8,
  transformObjectKeys: true
});

const obfuscatedJs = obfuscationResult.getObfuscatedCode();
console.log(`🔒 Código JavaScript ofuscado generado: ${(obfuscatedJs.length / 1024).toFixed(1)} KB`);

// 3. Encabezado legal
const legalHeader = `<!-- 
================================================================================
  ARCHIVO HSE - FOCUS HSE (Dirección Técnica: Adrián Arca)
  COPYRIGHT © 2026 FOCUS HSE. TODOS LOS DERECHOS RESERVADOS.
  Queda estrictamente prohibida la copia, clonación, ingeniería inversa o 
  redistribución comercial no autorizada del código fuente e investigaciones.
================================================================================
-->\n`;

// 4. Reensamblar HTML protegido
let protectedHtml = legalHeader + beforeScript + '\n' + obfuscatedJs + '\n' + afterScript;

fs.writeFileSync(distFile, protectedHtml, 'utf8');

console.log('✅ Archivo protegido generado exitosamente en:', distFile);
console.log(`📦 Tamaño final de index.html protegido: ${(protectedHtml.length / 1024).toFixed(1)} KB`);
