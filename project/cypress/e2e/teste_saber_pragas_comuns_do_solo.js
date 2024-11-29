describe('Teste Pragas Comuns Do Solo', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('Deve validar das pragas', () => {
        cy.get('[href="/crops/praga/"] > .icone_rodape').click();
        cy.url().should('include', '/crops/praga/');

        cy.get(':nth-child(1) .titulo-cartao').should('contain', 'Caramujos');
        cy.get(':nth-child(1) .botao-cartao').should('be.visible');

        cy.get(':nth-child(2) .titulo-cartao').should('contain', 'Lagarta');
        cy.get(':nth-child(2) .botao-cartao').should('be.visible');
    });

    it('Deve acessar a página de caramujos', () => {
        cy.get('[href="/crops/praga/"] > .icone_rodape').click();
        cy.url().should('include', '/crops/praga/');
        cy.get(':nth-child(1) .titulo-cartao').should('contain', 'Caramujos');
        cy.get(':nth-child(1) .botao-cartao').should('be.visible');
    });

    it('Deve acessar a página de lagartas', () => {
        cy.get('[href="/crops/praga/"] > .icone_rodape').click();
        cy.url().should('include', '/crops/praga/');
        cy.get(':nth-child(2) .titulo-cartao').should('contain', 'Lagarta');
        cy.get(':nth-child(2) .botao-cartao').should('be.visible');
    });


});
