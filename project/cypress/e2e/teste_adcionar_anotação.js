describe('Adicionar Anotação', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('Deve navegar para a página de configurações e clicar em Anotações', () => {
        cy.get('[href="/notas/meu_perfil/"] > .icone_rodape > .fas').click();
        cy.contains('Configurações').should('be.visible');
        cy.get('button').contains('Anotações').click();
        cy.url().should('include', '/notas/anotar');
    });

    it('Não deve adicionar anotação com conteúdo vazio', () => {
        cy.visit('http://127.0.0.1:8000/notas/anotar/');
        cy.get('textarea[name="conteudo"]').clear();
        cy.get('button[type="submit"]').click();
        cy.wait(5000);  
        cy.url().should('include', '/notas/anotar');  
    });

    it('Não deve adicionar anotação com apenas espaços em branco', () => {
        cy.visit('http://127.0.0.1:8000/notas/anotar/');
        cy.get('textarea[name="conteudo"]').clear().type('   ');  
        cy.get('button[type="submit"]').click();
        cy.contains('O conteúdo da anotação não pode ser vazio.').should('be.visible');  
        cy.url().should('include', '/notas/anotar');  
    });

    it('Deve adicionar anotação válida', () => {
        cy.visit('http://127.0.0.1:8000/notas/anotar/');
        cy.get('textarea[name="conteudo"]').clear().type('Minha nova anotação válida');  
        cy.get('button[type="submit"]').click();  
        cy.wait(5000); 

        cy.contains('Minha nova anotação válida').should('be.visible');  
        cy.url().should('include', '/notas/anotar'); 
    });
});
