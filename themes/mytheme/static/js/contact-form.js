// Shared Alpine.js contact-form component: name/email/message + a hidden
// honeypot field + Cloudflare Turnstile, POSTing to /api/contact. Used by
// both the landing page's Tailwind-styled modal (content/pages/landing*.html
// wrap the CTA button + modal in their own <div x-data="contactForm(...)">)
// and the blog's Bootstrap-styled modal (partials/contact_modal.html,
// included from partials/cta.html) - same submission behavior everywhere,
// framework-native markup per side (see CLAUDE.md's "two independent parts
// that never share templates" split - Tailwind/Bootstrap classes can't
// safely mix, so only the JS logic/behavior is shared, not the HTML).
//
// Success/error copy is passed in as arguments rather than hardcoded here:
// landing content files aren't run through Jinja (Pelican's HTMLReader only
// keeps <title>/<meta> from <head> and everything in <body> verbatim - see
// CLAUDE.md), so they can't reference UI_STRINGS - each one hardcodes its
// own translated strings directly in the x-data call. The blog side passes
// {{ t.contact_success|tojson }}/{{ t.contact_error|tojson }} instead.
function contactForm(successMessage, errorMessage) {
    return {
        showContactForm: false,
        formData: { name: '', email: '', message: '', company: '' },
        formStartedAt: 0,
        submitting: false,
        status: '',
        error: '',
        async submitContact(evt) {
            const SCRIPT_URL = '/api/contact';
            this.error = '';
            this.status = '';
            this.submitting = true;

            try {
                const turnstileToken = evt.target.querySelector('[name=cf-turnstile-response]')?.value || '';

                const body = new URLSearchParams({
                    ...this.formData,
                    startedAt: String(this.formStartedAt),
                    turnstileToken,
                }).toString();

                const res = await fetch(SCRIPT_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    },
                    body,
                });

                const data = await res.json().catch(() => ({}));

                if (!res.ok || !data.ok) {
                    throw new Error(data.error || 'Request failed');
                }

                this.formData = { name: '', email: '', message: '', company: '' };
                this.status = successMessage;
            } catch (err) {
                console.error(err);
                this.error = errorMessage;
            } finally {
                this.submitting = false;
                if (window.turnstile) window.turnstile.reset();
            }
        },
    };
}
