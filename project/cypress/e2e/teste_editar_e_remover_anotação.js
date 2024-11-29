describe('Teste Adicionar, Editar e Remover Anotação', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('Deve adicionar, editar e remover uma anotação', () => {
        cy.visit('http://127.0.0.1:8000/notas/anotar/');
        cy.get('textarea[name="conteudo"]').clear().type('Minha nova anotação válida');
        cy.get('button[type="submit"]').click();
        cy.contains('Minha nova anotação válida').should('be.visible');

        cy.get('ul > li').last().then((li) => {
            const notaId = li.find('a[href^="/notas/editar/"]').attr('href').match(/\/editar\/(\d+)\//)[1];

            cy.get('ul > li').last().find('.fa-edit').click();
            cy.url().should('include', `/notas/editar/${notaId}/`);
            cy.get('textarea[name="conteudo"]').clear().type('Minha anotação editada');
            cy.get('button[type="submit"]').click();
            cy.contains('Minha anotação editada').should('be.visible');

            cy.contains('Minha anotação editada').parent().find('.fa-trash-alt').click();
            cy.get('form > .botao').click();
        });
    });
});
