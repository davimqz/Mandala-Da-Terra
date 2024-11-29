describe('Editar e Remover Cultura', () => {
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
        cy.get('select[name="title"]').select('🍅 Tomate');
        cy.get('select[name="rua"]').select('Rua 1');
        cy.get('input[name="data_plantio"]').type('2024-12-01');
        cy.get('textarea[name="description"]').type('Plantar tomates para o inverno');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/crops/home');
        cy.get('.task-card').first().contains('Tomate🍅').should('be.visible');
        cy.get('.task-card').first().contains('Rua 1').should('be.visible');
        cy.get('.task-card').first().contains('Plantar tomates para o inverno').should('be.visible');
    });

    it('deve permitir editar a cultura mais recente', () => {
        cy.get('.task-card').first().find('.btn-edit').click();
        cy.get('textarea[name="description"]').clear().type('Descrição editada');
        cy.get('input[name="data_plantio"]').clear().type('2024-12-10');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/crops/home');
        cy.contains('Descrição editada').should('be.visible');
        cy.get('.task-card').first().contains('Data de Plantio: 10/12/2024').should('be.visible');
    });

    it('não deve permitir enviar sem data de plantio e descrição', () => {
        cy.get('.task-card').first().find('.btn-edit').click();
        cy.get('textarea[name="description"]').clear();
        cy.get('input[name="data_plantio"]').clear();
        cy.get('button[type="submit"]').click();
        cy.contains('Por favor, insira uma data de plantio e uma descrição').should('be.visible');
    });

    it('não deve permitir enviar sem data de plantio', () => {
        cy.get('.task-card').first().find('.btn-edit').click();
        cy.get('textarea[name="description"]').clear().type('Descrição válida');
        cy.get('input[name="data_plantio"]').clear();
        cy.get('button[type="submit"]').click();
        cy.contains('Por favor, insira a data de plantio').should('be.visible');
    });

    it('não deve permitir enviar sem descrição', () => {
        cy.get('.task-card').first().find('.btn-edit').click();
        cy.get('input[name="data_plantio"]').clear().type('2024-12-15');
        cy.get('textarea[name="description"]').clear();
        cy.get('button[type="submit"]').click();
        cy.contains('Por favor, insira uma descrição').should('be.visible');
    });

    it('deve permitir enviar quando ambos os campos estiverem preenchidos', () => {
        cy.get('.task-card').first().find('.btn-edit').click();
        cy.get('textarea[name="description"]').clear().type('Descrição válida');
        cy.get('input[name="data_plantio"]').clear().type('2024-12-15');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/crops/home');
    });

    it('deve remover a cultura mais recente ao clicar em "Marcar como colhido"', () => {
        cy.get('.task-card').first().find('.btn-remove').click();
    });
});
