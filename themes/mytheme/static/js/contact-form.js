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
        // Set on a successful submit so the modal can swap the form out for
        // a plain confirmation (see the `<template x-if="submitted">` /
        // `x-if="!submitted"` pair in each modal) instead of leaving the
        // now-empty form visible underneath the success message.
        submitted: false,
        status: '',
        error: '',
        autoCloseTimer: null,
        // Every "open" trigger (the CTA button on both sides) calls this
        // instead of setting showContactForm directly, so a fresh open
        // always starts from a clean slate - including cancelling a
        // still-pending auto-close timer from a previous submission the
        // visitor closed early and reopened before it fired.
        openContactForm() {
            if (this.autoCloseTimer) {
                clearTimeout(this.autoCloseTimer);
                this.autoCloseTimer = null;
            }
            this.submitted = false;
            this.status = '';
            this.error = '';
            this.showContactForm = true;
            this.formStartedAt = Date.now();
        },
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
                this.submitted = true;
                // Auto-close a couple seconds after the visitor sees the
                // confirmation, so they don't have to click anything.
                this.autoCloseTimer = setTimeout(() => {
                    this.showContactForm = false;
                }, 2500);
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
