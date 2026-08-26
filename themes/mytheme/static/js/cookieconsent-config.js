// Config for vanilla-cookieconsent (https://github.com/orestbida/cookieconsent),
// loaded as an ES module from the CDN by both base.html (blog theme) and
// landing.html. The theming (--cc-* variables, .cc--darkmode, .pm__* etc.)
// lives in landing.html's inline <style> and matches this library's class
// names exactly - see CLAUDE.md.
//
// Wired to Google Consent Mode v2: base.html/landing.html set
// 'analytics_storage' etc. to 'denied' by default before GTM loads: this
// file grants it once the visitor accepts the "analytics" category, via
// onFirstConsent/onChange below.
import * as CookieConsent from 'https://cdn.jsdelivr.net/npm/vanilla-cookieconsent@3/dist/cookieconsent.esm.js';

function detectLang() {
    var path = window.location.pathname;
    if (path.indexOf('/fr/') === 0 || path === '/fr') return 'fr';
    if (path.indexOf('/de/') === 0 || path === '/de') return 'de';
    if (path.indexOf('/es/') === 0 || path === '/es') return 'es';
    return 'en';
}

function updateGoogleConsent() {
    if (typeof window.gtag !== 'function') return;
    var granted = CookieConsent.acceptedCategory('analytics');
    window.gtag('consent', 'update', {
        analytics_storage: granted ? 'granted' : 'denied',
    });
}

CookieConsent.run({
    guiOptions: {
        consentModal: {
            layout: 'box',
            position: 'bottom left',
            equalWeightButtons: true,
            flipButtons: false,
        },
        preferencesModal: {
            layout: 'box',
            equalWeightButtons: true,
            flipButtons: false,
        },
    },
    categories: {
        necessary: {
            readOnly: true,
        },
        analytics: {},
    },
    language: {
        default: detectLang(),
        translations: {
            en: {
                consentModal: {
                    title: 'We use cookies',
                    description: 'We use cookies to understand how visitors use this site. You can accept all, reject non-essential ones, or manage your choice.',
                    acceptAllBtn: 'Accept all',
                    acceptNecessaryBtn: 'Reject all',
                    showPreferencesBtn: 'Manage preferences',
                    footer: '<a href="#">Privacy Policy</a>',
                },
                preferencesModal: {
                    title: 'Cookie preferences',
                    acceptAllBtn: 'Accept all',
                    acceptNecessaryBtn: 'Reject all',
                    savePreferencesBtn: 'Save preferences',
                    closeIconLabel: 'Close',
                    sections: [
                        {
                            title: 'Strictly necessary',
                            description: 'Required for the site to function properly. Cannot be disabled.',
                            linkedCategory: 'necessary',
                        },
                        {
                            title: 'Analytics',
                            description: 'Helps us understand how visitors use the site (Google Analytics via Google Tag Manager), so we can improve it.',
                            linkedCategory: 'analytics',
                        },
                    ],
                },
            },
            fr: {
                consentModal: {
                    title: 'Nous utilisons des cookies',
                    description: 'Nous utilisons des cookies pour comprendre comment ce site est utilisé. Vous pouvez tout accepter, tout refuser, ou choisir précisément.',
                    acceptAllBtn: 'Tout accepter',
                    acceptNecessaryBtn: 'Tout refuser',
                    showPreferencesBtn: 'Gérer mes préférences',
                    footer: '<a href="#">Politique de confidentialité</a>',
                },
                preferencesModal: {
                    title: 'Préférences des cookies',
                    acceptAllBtn: 'Tout accepter',
                    acceptNecessaryBtn: 'Tout refuser',
                    savePreferencesBtn: 'Enregistrer',
                    closeIconLabel: 'Fermer',
                    sections: [
                        {
                            title: 'Strictement nécessaires',
                            description: 'Indispensables au bon fonctionnement du site. Ne peuvent pas être désactivés.',
                            linkedCategory: 'necessary',
                        },
                        {
                            title: 'Analytique',
                            description: 'Nous aide à comprendre comment le site est utilisé (Google Analytics via Google Tag Manager), pour l\'améliorer.',
                            linkedCategory: 'analytics',
                        },
                    ],
                },
            },
            de: {
                consentModal: {
                    title: 'Wir verwenden Cookies',
                    description: 'Wir verwenden Cookies, um zu verstehen, wie diese Website genutzt wird. Sie können alle akzeptieren, ablehnen oder selbst auswählen.',
                    acceptAllBtn: 'Alle akzeptieren',
                    acceptNecessaryBtn: 'Alle ablehnen',
                    showPreferencesBtn: 'Einstellungen verwalten',
                    footer: '<a href="#">Datenschutzerklärung</a>',
                },
                preferencesModal: {
                    title: 'Cookie-Einstellungen',
                    acceptAllBtn: 'Alle akzeptieren',
                    acceptNecessaryBtn: 'Alle ablehnen',
                    savePreferencesBtn: 'Einstellungen speichern',
                    closeIconLabel: 'Schließen',
                    sections: [
                        {
                            title: 'Unbedingt erforderlich',
                            description: 'Für den Betrieb der Website erforderlich. Kann nicht deaktiviert werden.',
                            linkedCategory: 'necessary',
                        },
                        {
                            title: 'Analyse',
                            description: 'Hilft uns zu verstehen, wie die Website genutzt wird (Google Analytics über Google Tag Manager), um sie zu verbessern.',
                            linkedCategory: 'analytics',
                        },
                    ],
                },
            },
            es: {
                consentModal: {
                    title: 'Usamos cookies',
                    description: 'Usamos cookies para entender cómo se usa este sitio. Puedes aceptar todo, rechazar todo, o elegir tus preferencias.',
                    acceptAllBtn: 'Aceptar todo',
                    acceptNecessaryBtn: 'Rechazar todo',
                    showPreferencesBtn: 'Gestionar preferencias',
                    footer: '<a href="#">Política de privacidad</a>',
                },
                preferencesModal: {
                    title: 'Preferencias de cookies',
                    acceptAllBtn: 'Aceptar todo',
                    acceptNecessaryBtn: 'Rechazar todo',
                    savePreferencesBtn: 'Guardar preferencias',
                    closeIconLabel: 'Cerrar',
                    sections: [
                        {
                            title: 'Estrictamente necesarias',
                            description: 'Necesarias para el funcionamiento del sitio. No se pueden desactivar.',
                            linkedCategory: 'necessary',
                        },
                        {
                            title: 'Analíticas',
                            description: 'Nos ayuda a entender cómo se usa el sitio (Google Analytics vía Google Tag Manager), para mejorarlo.',
                            linkedCategory: 'analytics',
                        },
                    ],
                },
            },
        },
    },
    onFirstConsent: updateGoogleConsent,
    onChange: updateGoogleConsent,
});
