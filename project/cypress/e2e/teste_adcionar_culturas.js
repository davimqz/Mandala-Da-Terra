describe('Adicionar Cultura', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('deve permitir adicionar uma nova cultura', () => {
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
    });

    it('deve permitir adicionar uma nova cultura ao clicar no botão .botao_adicionar', () => {
        cy.get('.botao_adicionar').click(); 
        cy.get('select[name="title"]').select('Tomate🍅');
        cy.get('select[name="rua"]').select('Rua 1');
        cy.get('input[name="data_plantio"]').type('2024-12-01');
        cy.get('textarea[name="description"]').type('Plantar tomates para o inverno');
        cy.get('button[type="submit"]').click();
        
        cy.url().should('include', '/crops/home');
        cy.contains('Tomate🍅').should('be.visible');
        cy.contains('Rua 1').should('be.visible');
        cy.contains('Plantar tomates para o inverno').should('be.visible');
    });

    it('não deve permitir adicionar uma cultura sem data e descrição', () => {
        cy.get('[href="/crops/task/new/"] > .icone_rodape > .fas').click();
        cy.get('select[name="title"]').select('Tomate🍅');
        cy.get('select[name="rua"]').select('Rua 1');
        cy.get('button[type="submit"]').click();
        cy.contains('Por favor, insira uma data de plantio e uma descrição').should('be.visible');
    });

    it('não deve permitir adicionar uma cultura sem data de plantio, mas com descrição', () => {
        cy.get('[href="/crops/task/new/"] > .icone_rodape > .fas').click();
        cy.get('select[name="title"]').select('Tomate🍅');
        cy.get('select[name="rua"]').select('Rua 1');
        cy.get('textarea[name="description"]').type('Plantar tomates para o inverno');
        cy.get('button[type="submit"]').click();
        cy.contains('Por favor, insira uma data de plantio').should('be.visible');
    });

    it('não deve permitir adicionar uma cultura sem descrição, mas com data de plantio', () => {
        cy.get('[href="/crops/task/new/"] > .icone_rodape > .fas').click();
        cy.get('select[name="title"]').select('Tomate🍅');
        cy.get('select[name="rua"]').select('Rua 1');
        cy.get('input[name="data_plantio"]').type('2024-12-01');
        cy.get('button[type="submit"]').click();
        cy.contains('Por favor, insira uma descrição').should('be.visible');
    });
});
