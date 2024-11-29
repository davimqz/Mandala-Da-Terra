describe('Testar Tamanho Ideal Da Horta Baseada Na Quantidade De Pessoas', () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('input[name="email"]').type('a@gmail.com');
        cy.get('input[name="password"]').type('a');
        cy.get('button[type="submit"]').click();
        cy.url().should('include', '/home');
        cy.contains('Olá,').should('be.visible');
    });

    it('Deve verificar se não é possível calcular o tamanho da horta sem digitar nada', () => {
        cy.get('[href="/notas/meu_perfil/"] > .icone_rodape > .fas').click();
        cy.url().should('include', '/notas/meu_perfil');
        
        cy.get('button.tamanho-horta-btn').click();
        cy.get('input#numero1').should('be.visible');
        
        cy.get('button.tamanho-horta-btn').click();
        cy.get('#label_resultado').should('not.be.visible');
        cy.get('#resultado').should('not.be.visible');
    });

    it('Deve exibir um alerta ao tentar calcular com números negativos', () => {
        cy.get('[href="/notas/meu_perfil/"] > .icone_rodape > .fas').click();
        cy.url().should('include', '/notas/meu_perfil');
        
        cy.get('button.tamanho-horta-btn').click();
        
        cy.get('input#numero1').clear().type('-5');
        cy.get('button.tamanho-horta-btn').click();
        cy.on('window:alert', (alertText) => {
            expect(alertText).to.equal('Por favor, insira um número positivo!');
        });
    });

    it('Deve calcular corretamente o tamanho da horta com números positivos', () => {
        cy.get('[href="/notas/meu_perfil/"] > .icone_rodape > .fas').click();
        cy.url().should('include', '/notas/meu_perfil');
        
        cy.get('button.tamanho-horta-btn').click();
        
        cy.get('input#numero1').clear().type('5');
        cy.get('button.tamanho-horta-btn').click();
        cy.get('#label_resultado').should('be.visible');
        cy.get('#resultado').should('be.visible');
        cy.get('#resultado').should('have.value', '50');
    });
});
