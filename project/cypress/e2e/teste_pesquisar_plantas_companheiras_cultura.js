describe('Pesquisar Plantas Companheiras', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('Deve tentar pesquisar sem selecionar uma cultura e depois pesquisar uma cultura válida', () => {
        cy.get('[href="/crops/pesquisar/"] > .icone_rodape > .fas').click();
        cy.get('button[type="submit"]').click();        
        cy.wait(3000);
        cy.url().should('include', 'http://127.0.0.1:8000/crops/pesquisar/');

        cy.get('#opcoes').select('Batata🥔');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', 'http://127.0.0.1:8000/crops/pesquisar/?title=Batata%F0%9F%A5%94');
    });
});
