describe('Teste Dia Colheita', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('deve permitir adicionar uma nova cultura e mostrar a data de colheita', () => {
        cy.get('[href="/crops/task/new/"] > .icone_rodape > .fas').click();
        cy.get('select[name="title"]').select('Tomate🍅');
        cy.get('select[name="rua"]').select('Rua 1');
        cy.get('input[name="data_plantio"]').type('2024-12-01');
        cy.get('textarea[name="description"]').type('Plantar tomates para o inverno');
        cy.get('button[type="submit"]').click();

        cy.url().should('include', '/crops/home');

        cy.contains('Tomate🍅').should('be.visible');
        cy.contains('Rua 1').should('be.visible');
        cy.contains('Plantar tomates para o inverno').should('be.visible');
        
        cy.contains('Data de Plantio: 01/12/2024').should('be.visible');
        cy.contains('Data de Colheita: 01/03/2025').should('be.visible');
    });
});
